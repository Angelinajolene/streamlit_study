import streamlit as st
import pandas as pd
import numpy as np
import re
st.title("*STUDENT DETAILS*")
st.header("**Registration Form**")
select_box= st.sidebar.selectbox('Kindly provide all information',('Basic Information','Contact Details','Academic Details','Check'))
if select_box == "Basic Information":
    st.progress(25)

elif select_box == "Contact Details":
    st.progress(50)

elif select_box == "Academic Details":
    st.progress(75)

elif select_box == "Check":
    st.progress(100)
if(select_box=="Basic Information"):
    st.header("**Basic Information**")
    st.session_state.name= st.text_input("enter name")
    st.session_state.age= st.slider("age",5,20)
    st.session_state.gender= st.selectbox('choose an option',('Female','Male'))
    st.session_state.nationality = st.selectbox(
    'Select Nationality',
    ['Indian', 'American', 'British', 'Canadian', 'Australian',
     'Chinese', 'Japanese', 'German', 'French', 'Italian','Burmese']
)    
    if st.button("Next"):
        if not st.session_state.name.isalpha():
            st.error("Name should contain only alphabets") 
        elif st.session_state.name.strip() == "":
            st.error("Name cannot be empty")  
        elif st.session_state.age < 5:
            st.error("Age cannot be below 5")       
        else:
            st.write("Basic Informations saved ")   
elif(select_box =="Contact Details") :
    st.session_state.phone = st.text_input("Phone Number")
    st.session_state.email = st.text_input("Email")
    st.session_state.address = st.text_area("Address")
    if st.button("Next"):
        
            if not st. session_state.phone.isdigit():
                st.error("Phone number should contain only numbers")
            if len(st. session_state.phone) != 10:
                st.error("Phone number must contain 10 digits")   
            if len(set(st. session_state.phone)) == 1:
                st.error("Phone number cannot contain the same digit repeatedly") 
            elif len(st.session_state.address.strip()) < 10:
                st.error("Address must contain at least 10 characters")
            elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', st.session_state.email):
                st.error("Enter valid Gmail")
            else:
                st.write("Contact Informations saved ")  
    
elif(select_box=="Academic Details"):

    st.session_state.college = st.text_input("College Name")

    st.session_state.department = st.text_input("Department")

    st.session_state.cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )
    percentage = st.session_state.cgpa * 9.5

    st.write("Percentage:", percentage)

    data = pd.DataFrame({
    "Percentage": [0, percentage]
})

    st.line_chart(data)

    if st.button("Next"):

        if st.session_state.college.strip() == "":
            st.error("College name cannot be empty")

        elif st.session_state.department.strip() == "":
            st.error("Department cannot be empty")

        else:
            st.success("Academic Details Saved")
elif(select_box=="Check"):
    st.header("YOUR DETAILS")
    st.subheader("Basic information")
    st.write("*Name:*", st.session_state.name)
    st.write("*Age:*", st.session_state.age)
    st.write("*Gender:*", st.session_state.gender)
    st.header("Contact Details")
    st.write("*Phone:*",st.session_state.phone)
    st.write("*Email:",st.session_state.email)
    st.write("*Address:",st.session_state.address)
    st.header("Academic Details")
    st.write("*College Name:*",st.session_state.college)
    st.write("*Department:*",st.session_state.department)
    st.write("*CGPA:*",st.session_state.cgpa)
    
    






