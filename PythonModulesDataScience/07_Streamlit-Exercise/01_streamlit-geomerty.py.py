import streamlit as st

st.title("Calculator App using Streamlit")

# creates a horizontal line
st.write("---")

# input 1
num1 = st.number_input(label="Enter first number")

# input 2
num2 = st.number_input(label="Enter second number")

st.write("Operation")

operation = st.radio("Select an operation to perform:",
                     ("Add", "Subtract", "Multiply", "Divide"))

ans = 0


def calculate():
    if operation == "Add":
        ans = num1 + num2
    elif operation == "Subtract":
        ans = num1 - num2
    elif operation == "Multiply":
        ans = num1 * num2
    elif operation == "Divide" and num2 != 0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"

    st.success(f"Answer = {ans}")

if st.button("Calculate result"):
    calculate()