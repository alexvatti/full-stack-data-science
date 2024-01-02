import streamlit as st

def calculate_gross_salary(basic_salary, dearness_allowance=40, house_allowance=20):
    """
    Calculate the gross salary based on the basic salary, dearness allowance, and house allowance.

    Parameters:
    - basic_salary (float): Basic salary of the employee.
    - dearness_allowance (float): Percentage of dearness allowance (default is 40%).
    - house_allowance (float): Percentage of house allowance (default is 20%).

    Returns:
    - float: Gross salary.
    """
    gross_salary = basic_salary + (basic_salary * dearness_allowance / 100) + (basic_salary * house_allowance / 100)
    return gross_salary

if __name__ == "__main__":
    st.title("Gross Salary Calculator")

    basic_salary = st.number_input("Enter Basic Salary of employee: ")

    gross_salary_result = calculate_gross_salary(basic_salary)

    st.success(f"Basic Salary: {basic_salary} and Gross Salary: {gross_salary_result}")
