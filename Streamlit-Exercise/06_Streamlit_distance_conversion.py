import streamlit as st

def convert_distance(distance):
    """
    Convert distance from kilometers to meters, centimeters, feet, and inches.

    Parameters:
    - distance (float): Distance in kilometers.

    Displays:
    - Converted distances in meters, centimeters, feet, and inches.
    """
    meters = round(distance * 1000, 2)
    centimeters = round(distance * 100000, 2)
    feet = round(distance * 1093.61, 2)
    inches = round(distance * 25.4, 2)

    st.success(f"Given distance in km {distance} is converted in meters: {meters} meters")
    st.success(f"Given distance in km {distance} is converted in centimeters: {centimeters} centimeters")
    st.success(f"Given distance in km {distance} is converted in feet: {feet} feet")
    st.success(f"Given distance in km {distance} is converted in inches: {inches} inches")

if __name__ == "__main__":
    st.title("Distance Conversion App")

    distance = st.number_input("Enter distance between two cities (in km): ")

    convert_distance(distance)
