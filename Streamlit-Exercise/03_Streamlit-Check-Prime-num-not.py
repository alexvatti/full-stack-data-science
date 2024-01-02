import streamlit as st

def is_prime_number(num):
    """
    Check if a number is prime.

    Parameters:
    - num (int): The integer number to be checked.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def display_prime_result(num):
    """
    Display the result for whether a number is prime or not.

    Parameters:
    - num (int): The integer number to be displayed.
    """
    result_message = f"Number  {num} is {'a Prime' if is_prime_number(num) else 'not a Prime'} Number"
    st.success(result_message)

if __name__ == "__main__":
    st.title("Prime Number Checker")

    num = st.number_input("Enter an integer number: ", min_value=1, step=1)

    display_prime_result(num)

