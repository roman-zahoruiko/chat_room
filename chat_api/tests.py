from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Messages


class TestMessages(APITestCase):

    messages_list_url = reverse("messages_list", args=[0])
    messages_single_url = reverse("messages_single", args=[1])
    messages_add_url = reverse("messages_add")

    def setUp(self):
        self.client = APIClient()
        self.name = "test"
        self.email = "test@test.test"
        self.text = "test message"
        self.new_message = Messages.objects.create(author_username=self.name, author_email=self.email, text=self.text)

    def test_get_messages_list(self):
        response = self.client.get(self.messages_list_url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data[0].get("id"), 1)
        self.assertEqual(response.data[0].get("author_email"), self.email)
        self.assertEqual(response.data[0].get("text"), self.text)

    def test_get_message_single(self):
        response = self.client.get(self.messages_single_url)
        self.assertEqual(response.data["id"], 1)

    def test_post_message_add(self):
        body = {
            "author_username": "Test_post",
            "author_email": "test_post@test.test",
            "text": "Test_post",
        }
        response = self.client.post(self.messages_add_url, body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["id"], 2)
        self.assertEqual(response.data["text"], "Test_post")

    def test_post_message_add_wrong_data(self):
        body = {
            "author_email": "wrong@email@test",
            "text": "1" * 101,
        }
        response = self.client.post(self.messages_add_url, body)
        self.assertEqual(response.status_code, 400)
