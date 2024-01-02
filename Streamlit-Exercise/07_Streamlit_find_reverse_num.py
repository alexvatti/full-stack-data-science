import streamlit as st

def reverse_number(n):
    """
    Find the reverse of a given number.

    Parameters:
    - n (int): The integer number to be reversed.

    Returns:
    - int: The reversed number.
    """
    reversed_num = 0
    while n != 0:
        remainder = n % 10
        reversed_num = reversed_num * 10 + remainder
        n = n // 10
    return reversed_num

if __name__ == "__main__":
    st.title("Number Reversal App")

    input_number = st.number_input("Enter an integer number to find its reverse: ", min_value=1, step=1)

    reversed_result = reverse_number(input_number)

    st.success(f"Reverse of Given number {input_number} is {reversed_result}")
