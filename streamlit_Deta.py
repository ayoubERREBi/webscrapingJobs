#from typing import Pattern
import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta

Deta_KEY = "a0vqrphqnuy_v5zxxwmRDssLEJopgX3MvtS3ethfF9PM"

deta = Deta(Deta_KEY)

db = deta.Base("StreamlitAppDB")

def insert_user(email ,username,password):
  """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:

  """
  date_joined = str(datetime.datetime.now())
  return db.put({'key': email , 'username' : username,'password':password,'date_joined' : date_joined})

# insert_user('test@gmail.com','test','123456')

def fetch_users():
  """
  fetch Users
  :return Dictionary of users
  """
  users = db.fetch()
  return users.items

# print(fetch_users())
def get_user_emails():
  """
  fetch user Emails
  :return List of users emails
  """
  users = db.fetch()
  emails = []
  for user in users.items:
    emails.append(user['key'])
  return emails

# print(get_user_emails())

def get_usernames():
  """
  fetch usernames
  :return List of users usernames
  """
  users = db.fetch()
  usernames = []
  for user in users.items:
    usernames.append(user['username'])
  return usernames
# print(get_usernames())

def validate_email(email):
  """
  Check Email validity
  :param email
  :return True if email is valide else False
  """
  pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

  if re.match(pattern , email):
    return True
  return False
# print(validate_email("rabii@gmail.com"))

def validate_username(username):
  """
  checks validity of username
  :param username
  :return True if username is valid else False
  """
  pattern = "^[a-zA-Z0-9]+$"
  if re.match(pattern,username):
    return True
  return False
# print(validate_username("1brahim1"))

def sign_up():
  with st.form(key='signup',clear_on_submit=True):
    st.subheader(':green[Sign Up]')
    email = st.text_input(':blue[Email]', placeholder="Enter Your Email")
    username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
    password1 = st.text_input(':blue[Password]', placeholder="Enter Your Password", type='password')
    password2= st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')
    
    if email:
        if validate_email(email):
            if email not in get_user_emails():
                if validate_username(username):
                    if username not in get_usernames():
                        if len(username)>=2:
                            if len(password1)>=6:
                                if password1==password2:
                                    #add user
                                    hashed_password = stauth.Hasher([password2,]).generate()
                                    insert_user(email, username, hashed_password[0])
                                    st.success("Account created successfully !!")
                                    st.balloons()
                            else:
                                st.warning("password is too short")
                            
                        else:
                            st.warning('username is too short')
                    else:
                        st.warning("username already exists")
                else:
                    st.warning('invalid username')
            else:
                st.warning('Email already exists !!')
        else:
            st.warning('invalid Email')
    btn1,btn2,btn3,btn4,btn5 = st.columns(5)
    with btn3:
        st.form_submit_button('Sign Up')
                              
#sign_up()