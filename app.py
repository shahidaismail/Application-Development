import streamlit as st
st.header("students grouping app")
st.write("choose a group according to your gender")

gender = st.text_input("male","female")

col1,col2 = st.columns(2)

with col1:
    if st.button("male"):
        st.write("go to group A")
        
with col2:
    if st.button("female"):
        st.write("go to group B")
        


             


