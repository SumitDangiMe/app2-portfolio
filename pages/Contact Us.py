import streamlit as st
from email_sender import send_email
st.title('Contact Us')
with st.form(key='email_forms'):
    email = st.text_input('Your Email Address')
    message = st.text_area('Your Message')
    button = st.form_submit_button('Submit')
    if button:
        send_email(email,message)
        st.info('Email sent successfully')
