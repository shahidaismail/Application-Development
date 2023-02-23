import streamlit as st

st.header("students grouping form")
gender = "male,female"
gender = input("what is your gender")

col1,col2 = columns(2)

if gender is male:
    print(col1)
if gender is female:
    print(col2)


