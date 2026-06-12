import streamlit as st
from datetime import datetime
from library import gen_random_int, create_string, my_sort

st.set_page_config(
    page_title="Exercise 1"
)

st.header("Exercise 1")


def generate():
    seed = int(datetime.now().timestamp())
    array: list[int] = gen_random_int(10, seed)
    array_str: str = create_string(array)
    st.session_state['numbers'] = array_str
    st.session_state['sorted_numbers'] = ""


def sort_generated_numbers():
    numbers: str = st.session_state.get("numbers", "")
    if not numbers:
        st.session_state['sorted_numbers'] = ""
        return

    array_int: list[int] = [int(number.strip()) for number in numbers.rstrip(".").split(",") if number.strip()]
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

st.button("Generate", on_click=generate)

st.write("Generated Numbers:", st.session_state['numbers'])

st.button("Sort", on_click=sort_generated_numbers)

st.write("Sorted Numbers:", st.session_state['sorted_numbers'])

# this code is provided to clear the page
st.button("Clear", on_click=clear)
