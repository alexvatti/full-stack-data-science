import streamlit as st

def count_words(text):
    """
    Count the number of words in a given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - int: Number of words in the text.
    """
    return len(text.split())

if __name__ == "__main__":
    st.title("Words Count App Using Streamlit")

    input_text = st.text_input("Enter a text to find the number of words: ")

    words_count = count_words(input_text)

    st.success(f"Number of words: {words_count}")

