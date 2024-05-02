1. Please install the packages mentioned in the requirements.txt file.
   There are some additional packages which helps us improve the development.

    pip install -r requirements.txt

2. Please create a user. Token for the user will get auto generated as a signal is defined for it. 
   Since no schema was provided how a user will be related to any other model, I assumed it to be used only for the purpose of token based authentication.

   To get a token for a user to access the API endpoints, follow below steps in Django's.

   1. User.objects.create(username="ash", email="ash@gmail.com", first_name="ash", last_name="jare", password="12345")
   2. u=_
   3. u.auth_token.key

   3rd statement will print the token on token. copy the token and add it in the POSTMAN's headers.
   Header KEY - Authorization
   Header VALUE - token <value-of-copied-token>

3. After following above steps, we can successfully start testing the project.

NOTE: 
    1. Since the UI was not mentioned and due to time constraints I had from my end (due to my current job), I chose not to use a Frontend technology to develope the project.
    2. I wanted to setup Docker but again, due to time constraints from my side, I couldn't implement it.

