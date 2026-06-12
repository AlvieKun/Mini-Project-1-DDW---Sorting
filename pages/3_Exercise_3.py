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

    div[data-testid="stTextInput"] input {
        background: #171b24;
        border: 1px solid #303746;
        color: #f5f7fb;
        border-radius: 8px;
    }

    div[data-testid="stSlider"] {
        background: #171b24;
        border: 1px solid #303746;
        border-radius: 10px;
        padding: 1rem 1rem 0.6rem;
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

    .star-preview {
        text-align: center;
        padding: 0.8rem 1rem;
        margin: 0.75rem 0 0.75rem;
        border: 1px solid #303746;
        border-radius: 10px;
        background: #171b24;
    }

    .star-preview .stars {
        color: #f5a623;
        font-size: 2.4rem;
        line-height: 1.15;
        letter-spacing: 0;
        font-weight: 800;
    }

    .star-preview .rating-copy {
        color: #b8c0cc;
        margin-top: 0.2rem;
        font-weight: 600;
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


def rating_to_stars(rating: float) -> str:
    full_stars = int(rating)
    has_half_star = rating - full_stars >= 0.5
    empty_stars = 5 - full_stars - int(has_half_star)
    return "★" * full_stars + ("½" if has_half_star else "") + "☆" * empty_stars


default_ideas = [
    {"idea": "AI Study Planner", "category": "Education", "rating": 4.5},
    {"idea": "Campus Food Finder", "category": "Student Life", "rating": 3.5},
    {"idea": "Accessibility Route Planner", "category": "Social Impact", "rating": 5.0},
    {"idea": "Smart Recycling Bin", "category": "Sustainability", "rating": 4.0},
]

if "ideas" not in st.session_state:
    st.session_state.ideas = default_ideas[:]

if "sorted_ideas" not in st.session_state:
    st.session_state.sorted_ideas = []

if "idea_rating" not in st.session_state:
    st.session_state.idea_rating = 3.0


def add_idea():
    idea = st.session_state.get("idea_name", "").strip()
    category = st.session_state.get("idea_category", "").strip()
    rating = float(st.session_state.get("idea_rating", 3.0))

    if not idea:
        st.warning("Please enter a project idea name.")
        return

    if not category:
        st.warning("Please enter a category.")
        return

    st.session_state.ideas.append(
        {"idea": idea, "category": category, "rating": rating}
    )
    st.session_state.idea_name = ""
    st.session_state.idea_category = ""
    st.session_state.sorted_ideas = []
    st.success(f"Added '{idea}' with a {rating:.1f}-star rating.")


def sort_ideas():
    st.session_state.sorted_ideas = comb_sort_ideas(st.session_state.ideas)


def reset_ideas():
    st.session_state.ideas = default_ideas[:]
    st.session_state.sorted_ideas = []
    st.session_state.idea_name = ""
    st.session_state.idea_category = ""
    st.session_state.idea_rating = 3.0


st.title("Project Idea Ranker")
st.write(
    "Rate project ideas out of 5 stars and sort them from highest-rated "
    "to lowest-rated using Comb Sort."
)

st.header("Add a Project Idea")
st.text_input("Project idea name", key="idea_name")
st.text_input("Category", key="idea_category")
rating = st.slider(
    "Drag to rate this idea",
    min_value=0.5,
    max_value=5.0,
    value=3.0,
    step=0.5,
    key="idea_rating",
)
st.markdown(
    f"""
    <div class="star-preview">
        <div class="stars">{rating_to_stars(rating)}</div>
        <div class="rating-copy">{rating:.1f} out of 5 stars</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.button("Add Idea", on_click=add_idea)

st.header("Original Ideas")
st.table(st.session_state.ideas)

st.header("Actions")
st.button("Sort by Rating", on_click=sort_ideas)
st.button("Reset", on_click=reset_ideas)

st.header("Sorted Ideas")
if st.session_state.sorted_ideas:
    st.table(st.session_state.sorted_ideas)
else:
    st.markdown(
        '<div class="empty-ranking">Click Sort by Rating to rank the ideas.</div>',
        unsafe_allow_html=True,
    )
