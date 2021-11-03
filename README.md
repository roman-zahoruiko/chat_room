# chat_room (test task)
Django application - public chat room(only RESTful API).

###Basic requirements:
- Django, Django REST Framework, PostgreSQL
- The message must contain author(unauthenticated user) email and text, create date and update date.
- Email validation (regex to check if that is real email)
- Message validation (regex to check if message is not empty string, and length < 100)

###API methods:
- GET method for getting all messages with pagination by 10 messages per request.
  - e.g.
  - /api/messages/list/0 will return first 10 messages
  - /api/messages/list/1 will return second 10 messages
  etc
- GET method for getting single message by unique identifier
e.g.
/api/messages/single/123
  - POST method for creating a new message
  Body accepts email and text.
- Add request validators
- API documentation(preferably with sandbox for sending requests, e.g. Swagger)
- Deploy to Heroku


## You can check the documentation at the link below:
### https://chatroom-roman-z.herokuapp.com/