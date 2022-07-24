import streamlit as st

# st.title('Multiplication of 2 numbers')
# a = st.number_input('Enter a number')
# b = st.number_input('Enter another number')
# result = a * b
# st.write(a, ' * ', b , '= ', result)

st.title('Finding whether the given number is odd or even')
a = st.number_input('Enter a number')
if(a%2==0):
  result = "even number"
else :
  result = "odd number"
st.write(a, ' is an', result)