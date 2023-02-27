import streamlit as st
st.title('sakshi m')
st.header(':red[Data Science Intern]')
st.subheader(":blue[Innomatics Research labs]")

btn_click = st.button("details about me...click here")
if btn_click == True:
    st.subheader("hiiii nice to meet you i am sakshi")
    st.caption('i m currently studying computer engineering and learning data science')

    st.subheader('My linkedin and Github profiles are as follows')


    st.markdown('Linkedin : https://www.linkedin.com/in/sakshimahajan032002/')
    st.markdown('GitHub: https://github.com/Sakshi27m')