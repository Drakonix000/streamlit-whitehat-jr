import streamlit as st
num = 4
st.write("Square of ", num, " is ", num**2)

slider = st.slider("Choose your number", 1, 100)
st.write("Square of ", slider, " is ", slider**2)

