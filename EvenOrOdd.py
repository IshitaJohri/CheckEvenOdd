import streamlit as st

st.title('Finding whether the given number is odd or even')
a = st.number_input('Enter a number')
if(a%2==0):
  result = "even number"
else :
  result = "odd number"
st.write(a, ' is an', result)
