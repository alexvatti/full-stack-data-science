import streamlit as st

def calculate_total_and_percentage(subject_marks):
    """
    Calculate the total marks and percentage obtained.

    Parameters:
    - subject_marks (list): List containing marks of 5 subjects.

    Returns:
    - tuple: Total marks and percentage.
    """
    total_marks = sum(subject_marks)
    percentage = round(total_marks / len(subject_marks), 2)
    return total_marks, percentage

if __name__ == "__main__":
    st.title("Subject Marks Calculator")

    subject_1_marks = st.number_input("Enter Subject 1 Marks (Min-0 - Max 100): ", min_value=0, max_value=100)
    subject_2_marks = st.number_input("Enter Subject 2 Marks (Min-0 - Max 100): ", min_value=0, max_value=100)
    subject_3_marks = st.number_input("Enter Subject 3 Marks (Min-0 - Max 100): ", min_value=0, max_value=100)
    subject_4_marks = st.number_input("Enter Subject 4 Marks (Min-0 - Max 100): ", min_value=0, max_value=100)
    subject_5_marks = st.number_input("Enter Subject 5 Marks (Min-0 - Max 100): ", min_value=0, max_value=100)

    subject_marks_list = [subject_1_marks, subject_2_marks, subject_3_marks, subject_4_marks, subject_5_marks]

    total_marks, percentage = calculate_total_and_percentage(subject_marks_list)

    st.success(f"Sum of Marks: {total_marks} and Percentage: {percentage}% obtained by the student")
