import streamlit as st
from library import create_string, my_sort

st.set_page_config(
    page_title="Exercise 2"
)

st.header("Exercise 2")


def sort_numbers():
    numbers: str = st.session_state.get("numbers", "")
    if not numbers.strip():
        st.session_state['sorted_numbers'] = ""
        return

    try:
        array_int: list[int] = [int(number.strip()) for number in numbers.split(",") if number.strip()]
    except ValueError:
        st.session_state['sorted_numbers'] = ""
        st.error("Please enter only integers separated by commas.")
        return

    my_sort(array_int)
    array_str: str = create_string(array_int)
    st.session_state['sorted_numbers'] = array_str


def clear():
    st.session_state['numbers'] = ""
    st.session_state['sorted_numbers'] = ""

if 'numbers' not in st.session_state:
    st.session_state.numbers = ""

if 'sorted_numbers' not in st.session_state:
    st.session_state.sorted_numbers = ""

st.text_input("Enter integers separated by comma:", key="numbers")

st.button("Sort", on_click=sort_numbers)

st.write("Sorted Numbers:", st.session_state['sorted_numbers'])

st.button("Clear", on_click=clear)
