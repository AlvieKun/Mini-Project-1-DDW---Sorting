import streamlit as st
from library import comb_sort_ideas

st.set_page_config(
    page_title="Exercise 3"
)

st.markdown(
    """
    <style>
    .stApp {
        background: #0f1117;
        color: #f5f7fb;
    }

    .block-container {
        max-width: 980px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #f5f7fb !important;
        letter-spacing: 0 !important;
    }

    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stCaptionContainer"] {
        color: #b8c0cc;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        background: #171b24;
        border: 1px solid #303746;
        color: #f5f7fb;
        border-radius: 8px;
    }

    div[data-testid="stButton"] > button {
        border: 1px solid #3a4354;
        border-radius: 8px;
        background: #202635;
        color: #f5f7fb;
        font-weight: 700;
    }

    div[data-testid="stButton"] > button:hover {
        border-color: #f5a623;
        color: #ffffff;
        background: #2a3142;
    }

    div[data-testid="stTable"] {
        border: 1px solid #303746;
        border-radius: 10px;
        overflow: hidden;
    }

    .empty-ranking {
        padding: 0.85rem 1rem;
        border-radius: 8px;
        background: #171b24;
        border: 1px solid #303746;
        color: #b8c0cc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Each item is a project idea record containing non-numeric text data.
default_ideas = [
    {
        "idea": "Campus Food Finder",
        "category": "Student Life",
        "description": "Finds affordable food near campus",
    },
    {
        "idea": "Accessibility Route Planner",
        "category": "Social Impact",
        "description": "Helps users find accessible routes",
    },
    {
        "idea": "AI Study Planner",
        "category": "Education",
        "description": "Creates study plans for students",
    },
    {
        "idea": "Smart Recycling Bin",
        "category": "Sustainability",
        "description": "Sorts recycling items more easily",
    },
]

if "ideas" not in st.session_state:
    st.session_state.ideas = default_ideas[:]

if "sorted_ideas" not in st.session_state:
    st.session_state.sorted_ideas = []


def add_idea():
    idea = st.session_state.get("idea_name", "").strip()
    category = st.session_state.get("idea_category", "").strip()
    description = st.session_state.get("idea_description", "").strip()

    if not idea:
        st.warning("Please enter a project idea name.")
        return

    if not category:
        st.warning("Please enter a category.")
        return

    st.session_state.ideas.append(
        {"idea": idea, "category": category, "description": description}
    )
    st.session_state.idea_name = ""
    st.session_state.idea_category = ""
    st.session_state.idea_description = ""
    st.session_state.sorted_ideas = []
    st.success(f"Added '{idea}' to the directory.")


def sort_ideas():
    # Comb Sort compares idea names alphabetically. No built-in sort is used.
    st.session_state.sorted_ideas = comb_sort_ideas(st.session_state.ideas)


def reset_ideas():
    st.session_state.ideas = default_ideas[:]
    st.session_state.sorted_ideas = []
    st.session_state.idea_name = ""
    st.session_state.idea_category = ""
    st.session_state.idea_description = ""


st.title("Project Idea Directory")
st.write("Add project ideas and sort them alphabetically from A to Z using Comb Sort.")

st.header("Add a Project Idea")
st.text_input("Project idea name", key="idea_name")
st.text_input("Category", key="idea_category")
st.text_area("Short description", key="idea_description")

st.button("Add Idea", on_click=add_idea)

st.header("Original Ideas")
st.table(st.session_state.ideas)

st.header("Actions")
st.button("Sort Alphabetically", on_click=sort_ideas)
st.button("Reset", on_click=reset_ideas)

st.header("Sorted Ideas")
if st.session_state.sorted_ideas:
    st.table(st.session_state.sorted_ideas)
else:
    st.markdown(
        '<div class="empty-ranking">Click Sort Alphabetically to organize the ideas.</div>',
        unsafe_allow_html=True,
    )
