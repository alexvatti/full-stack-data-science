import streamlit as st

def sum_first_last_digit(number):
    """
    Calculate the sum of the first and last digit of a 4-digit number.

    Parameters:
    - number (int): The 4-digit number.

    Returns:
    - int: Sum of the first and last digit.
    """
    digits = []
    while number != 0:
        remainder = number % 10
        digits.append(remainder)
        number = number // 10
    digits.reverse()
    return digits[0] + digits[-1]

if __name__ == "__main__":
    st.title("Sum of First and Last Digit Calculator")

input_number = st.number_input("Enter an integer number (1000 to 9999): ", min_value=1000, max_value=9999, step=1)

    if 1000 >= input_number <= 9999:
        if st.button("Submit"):
            result = sum_first_last_digit(input_number)
            st.success(f"Sum of the first and last digit of given number {input_number} is {result}")
    else:
        st.success("Invalid Input. Please enter a number between 1000 and 9999.")
