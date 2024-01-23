import streamlit as st
import streamlit_authenticator as stauth
from streamlit_Deta import sign_up,fetch_users
import smtplib

def send_email(sender,reciver,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(sender,"lass rpof vemd odab")

    server.sendmail(sender, reciver, message)

st.set_page_config(page_title='WISD',page_icon='💰',initial_sidebar_state='collapsed')
try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []
    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])
    
    credentials = {'usernames':{}}
    
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name':emails[index],'password':passwords[index]}              
    
    #print(credentials)
    Authenticator =  stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef',cookie_expiry_days=4) 
    
    email,authentication_status,username = Authenticator.login(':green[login]','main')
       
    
    info,info1 = st.columns(2)
    
    if not authentication_status:
        st.subheader('')
        sign_up()
        #st.write("Don't have an account.")
        #signup_button = st.button("Sign up")

    #if signup_button:
     #   sign_up()
        
    
    if username:
        if username in usernames:
            if authentication_status:
                #______________________login successfully_________________________________________________
                st.subheader('Welcome To WISD Intership ')
                
                
                from FetchJobs import fetch_jobs
                # Fetch jobs from Deta
                jobs = fetch_jobs()

                # Streamlit App
                st.title("job list for last 7 days")

                # Afficher les jobs sous forme de liste avec des liens cliquables
                if jobs:
                    for job in jobs:
                        if job['datePublish'] < 7:
                            # Créer un lien cliquable pour chaque job
                            link = f"[{job['jobTitles']} chez {job['companyName']}]({job['jobLinks']})"
                            st.markdown(link, unsafe_allow_html=True)
                #__________________________send jobs via email______________________________________
                            email_acc=emails[usernames.index(username)]
                            
            
                            sender = "workchannel14@gmail.com"
                            reciver = email_acc
            
                            subject = "WISD internship 2024"
                            message = f"Offre du jour : {job['jobTitles']} chez {job['companyName']}. Lien : {job['jobLinks']}"
                            
                            subject = subject.encode('utf-8')
                            message = message.encode('utf-8')
                            
                            text = f"Subject: {subject}\n\n{message}"
                            
                            send_email(sender, reciver, text)
                #__________________________________________________________________________________
                else:
                    st.write("Aucun job trouvé.")
                
                
                
                st.sidebar.write(f'Welcome {username}')
                Authenticator.logout('Log Out','sidebar')
                #let user see app_________________________________________________________________________
            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist , Please Sign up')
    
except Exception as error:
    st.warning(f'Error: {error}')
    