# Import Streamlit
import streamlit as st
import math

st.title("Adding two numbers!")

# sidebar input
num1 = st.sidebar.number_input('Enter first number', value=0, format="%i")
num2 = st.sidebar.number_input('Enter second number', value=0, format="%i")

# operation
total = num1 + num2

# calculate square root
sqrt_total = math.sqrt(total)

# main page display
st.write(f"The total of {num1} and {num2} is {total}.")
st.write(f"The square root of the total ({total}) is {sqrt_total}.")

