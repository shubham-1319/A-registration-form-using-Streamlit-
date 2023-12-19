#created by Shubh
import streamlit as st

def registration_form():
    st.title('Registration Form')

    roll_no = st.text_input('Roll No.')
    dob = st.date_input('Date of Birth')
    name = st.text_input('Name')
    last_name = st.text_input('Last Name')
    branch = st.selectbox('Branch', ['Select Branch', 'Computer Science', 'Electrical Engineering', 'Mechanical Engineering'])

    if st.button('Submit'):
        if roll_no and dob and name and last_name and branch != 'Select Branch':
            st.success('Registration successful!')
            st.write('Roll No.:', roll_no)
            st.write('Date of Birth:', dob)
            st.write('Name:', name)
            st.write('Last Name:', last_name)
            st.write('Branch:', branch)
        else:
            st.warning('Please fill in all the fields!')

if __name__ == '__main__':
    registration_form()
