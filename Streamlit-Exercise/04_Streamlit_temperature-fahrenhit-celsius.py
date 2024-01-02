import streamlit as st

def fahrenheit_to_celsius(temp_f):
    """
    Convert Fahrenheit temperature to Celsius.

    Parameters:
    - temp_f (float): Temperature in Fahrenheit.

    Returns:
    - float: Temperature in Celsius.
    """
    celsius = (temp_f - 32) * 5/9
    return celsius

if __name__ == "__main__":
    st.title("Temperature Converter")

    temp_f = st.number_input("Enter temperature in Fahrenheit: ", min_value=-50, max_value=250)

    celsius_temp = fahrenheit_to_celsius(temp_f)
    st.success(f"Temperature in Celsius: {round(celsius_temp, 2)}")
