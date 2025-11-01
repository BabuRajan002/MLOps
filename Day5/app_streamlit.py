import streamlit as st
st.title('Interactive streamlit app')
name = st.text_input('Enter your name:')
if name:
    st.write(f"Hello, {name}!")
    
number = st.slider("Select a number:",0,100,500)
number1 = st.checkbox("I agree")

st.write(f"You selected: {number}")

if st.button('Greet'):
    st.write('Greetings from the streamlit')

         

