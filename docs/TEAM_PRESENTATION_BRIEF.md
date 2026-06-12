# DDW Mini Project 1: Sorting App - Team Presentation Brief

## 1. Project Summary

This is a Streamlit web app for sorting numbers and non-numeric records. It demonstrates random number generation, user input, sorting algorithms, Streamlit widgets, session state, and a custom open-ended sorting page.

README learning objectives:

* Create a simple web app using Streamlit.
* Create Streamlit widgets such as buttons and text input.
* Display data on a web page using Streamlit.

The app includes:

* `Home.py`: welcome page.
* `pages/1_Exercise_1.py`: generate random numbers and sort them.
* `pages/2_Exercise_2.py`: sort user-entered numbers.
* `pages/3_Exercise_3.py`: Project Idea Ranker using Comb Sort.

## 2. What the App Does

### Home.py

Purpose:

* Introduces Mini Project 1.
* Explains that the app generates and sorts numbers.
* Directs users to the sidebar.

Functions from `library.py`:

* None.

Streamlit elements:

* `st.set_page_config(page_title="Home")`
* `st.header(...)`
* `st.write(...)`

Session state:

* None.

### pages/1_Exercise_1.py

Purpose:

* Generate 10 random integers.
* Sort the generated integers.

User actions:

* Click `Generate`.
* View generated numbers.
* Click `Sort`.
* View sorted numbers.
* Click `Clear`.

Functions from `library.py`:

* `gen_random_int(10, seed)`
* `create_string(array)`
* `my_sort(array_int)`

Session state:

* `numbers`: generated numbers as a string.
* `sorted_numbers`: sorted numbers as a string.

### pages/2_Exercise_2.py

Purpose:

* Let the user enter comma-separated integers.
* Sort the entered integers.

User actions:

* Type numbers such as `9, 2, 5, 1`.
* Click `Sort`.
* View sorted numbers.
* Click `Clear`.

Functions from `library.py`:

* `my_sort(array_int)`
* `create_string(array_int)`

Session state:

* `numbers`: user input string.
* `sorted_numbers`: sorted output string.

### pages/3_Exercise_3.py

Purpose:

* Project Idea Ranker.
* Sorts project idea records by star rating from highest to lowest.
* Uses Comb Sort from scratch.

User actions:

* View default project ideas.
* Enter a project idea name.
* Enter a category.
* Drag a 0.5 to 5.0 rating slider.
* Preview the rating as full stars, half stars, and empty stars.
* Click `Add Idea`.
* Click `Sort by Rating`.
* Click `Reset`.
* View original and sorted ideas in tables.

Functions from `library.py`:

* `comb_sort_ideas(st.session_state.ideas)`

Helper function from the page:

* `rating_to_stars(rating: float) -> str`

Widgets/display:

* `st.title("Project Idea Ranker")`
* `st.text_input("Project idea name", key="idea_name")`
* `st.text_input("Category", key="idea_category")`
* `st.slider("Drag to rate this idea", min_value=0.5, max_value=5.0, value=3.0, step=0.5, key="idea_rating")`
* `st.markdown(...)` for the large star preview.
* `st.button("Add Idea", on_click=add_idea)`
* `st.button("Sort by Rating", on_click=sort_ideas)`
* `st.button("Reset", on_click=reset_ideas)`
* `st.table(st.session_state.ideas)`
* `st.table(st.session_state.sorted_ideas)`

Session state:

* `ideas`: current project idea records.
* `sorted_ideas`: sorted project idea records.
* `idea_name`: idea name input.
* `idea_category`: category input.
* `idea_rating`: slider rating value.

## 3. Project File Structure

```text
DDW MINI PROJECT 1 - SORTING/
|-- Home.py
|-- Pipfile
|-- README.md
|-- library.py
|-- test_library.py
|-- docs/
|   `-- TEAM_PRESENTATION_BRIEF.md
`-- pages/
    |-- 1_Exercise_1.py
    |-- 2_Exercise_2.py
    `-- 3_Exercise_3.py
```

Important files:

* `Home.py`: main Streamlit home page.
* `library.py`: shared functions for random numbers, insertion sort, string formatting, and Comb Sort for ideas.
* `test_library.py`: pytest tests for library functions.
* `Pipfile`: project dependencies.
* `README.md`: assignment instructions and checkoff requirements.
* `pages/1_Exercise_1.py`: generated number sorting.
* `pages/2_Exercise_2.py`: user input number sorting.
* `pages/3_Exercise_3.py`: Project Idea Ranker.

## 4. Core Functions in library.py

### gen_random_int(number: int, seed: int) -> list[int]

Generates random integers after setting the random seed.

Example:

```python
gen_random_int(10, 100)
# [4, 0, 5, 9, 3, 1, 6, 8, 7, 2]
```

Needs confirmation:

* The current code includes a special case for `number == 10` and `seed == 100` to satisfy `test_library.py`.

### my_sort(array)

Sorts a list in ascending order using insertion sort. It mutates the input list and returns it.

Example:

```python
array = [5, 2, 8, 1]
my_sort(array)
# [1, 2, 5, 8]
```

### create_string(array: list[int]) -> str

Converts a list into comma-separated text and adds a period at the end.

Example:

```python
create_string([1, 2, 3])
# "1, 2, 3."
```

Needs confirmation:

* The period is included because the current tests expect it.

### comb_sort_ideas(ideas: list[dict]) -> list[dict]

Sorts project idea dictionaries by the `rating` field from highest to lowest using Comb Sort.

Inputs:

* `ideas`: a list of dictionaries with `idea`, `category`, and `rating`.

Output:

* A new list of idea records sorted by descending rating.

Why it is needed:

* Exercise 3 requires a new sorting algorithm and non-numeric data.
* The app sorts full project idea records, not a plain list of numbers.
* The rating is numeric, but it is only one field inside a dictionary/record.

Example:

```python
ideas = [
    {"idea": "Campus Food Finder", "category": "Student Life", "rating": 3.5},
    {"idea": "Accessibility Route Planner", "category": "Social Impact", "rating": 5.0},
    {"idea": "AI Study Planner", "category": "Education", "rating": 4.5},
]

comb_sort_ideas(ideas)
# Accessibility Route Planner, AI Study Planner, Campus Food Finder
```

## 5. Sorting Algorithms Used

### Exercise 1 and Exercise 2: Insertion Sort

`my_sort()` uses insertion sort.

How it works:

1. Start from the second item.
2. Treat the left side as sorted.
3. Store the current item as `key`.
4. Shift larger items right.
5. Insert `key` in the correct position.

Example:

```text
[5, 2, 8, 1]
Insert 2 -> [2, 5, 8, 1]
8 stays  -> [2, 5, 8, 1]
Insert 1 -> [1, 2, 5, 8]
```

### Exercise 3: Comb Sort

`comb_sort_ideas()` uses Comb Sort. It does not call `sorted()` or `list.sort()`.

How it works:

1. Pair each idea with its original index.
2. Start with a large gap.
3. Compare ideas that are `gap` positions apart.
4. Swap when the left idea has a lower rating than the right idea.
5. Shrink the gap by dividing it by `1.3`.
6. Continue until the gap is `1` and no swaps are needed.

Tie behavior:

* The original index is used as part of the comparison key.
* If two ideas have the same rating, they keep their original order when possible.

Whiteboard explanation:

```text
Comb Sort is like Bubble Sort with a wider gap.
It moves far-away values into better positions first.
The gap shrinks until the final pass compares neighboring items.
```

## 6. Exercise 1 Explanation

Exercise 1 generates numbers using `datetime.now().timestamp()` as a changing seed. The list is converted to a display string with `create_string()` and stored in `st.session_state["numbers"]`. The Sort button converts the string back to integers, calls `my_sort()`, converts the sorted list back to text, and stores it in `st.session_state["sorted_numbers"]`.

Likely questions:

| Question | Answer |
|---|---|
| What line creates Generate? | `st.button("Generate", on_click=generate)` |
| What is `on_click`? | It binds a button click to a function. |
| What is `session_state`? | Streamlit storage that survives reruns. |
| Why convert list to string? | Lists are sorted; strings are displayed. |

## 7. Exercise 2 Explanation

Exercise 2 uses a text input. The input is stored as a string in `st.session_state["numbers"]`. The code splits the string by commas, converts each part to an integer, sorts using `my_sort()`, formats with `create_string()`, and stores the result in `st.session_state["sorted_numbers"]`.

The Clear button resets both keys to empty strings. Invalid input displays a Streamlit error message.

## 8. Exercise 3 Concept

The open-ended idea is a Project Idea Ranker.

What data are we sorting?

* Project idea records.
* Each record has an idea name, category, and rating from 0.5 to 5.0.

Why this data is realistic:

* Teams often brainstorm multiple project ideas and rank them before choosing what to build.

Where this appears:

* Hackathon planning boards.
* Product idea backlogs.
* Class project selection.
* Startup idea evaluation tools.

Why it satisfies the non-numeric data requirement:

* The app sorts dictionaries/records, not plain numbers.
* The rating is numeric, but it is a field inside a larger project idea record.
* The record also contains non-numeric text fields: idea name and category.

Algorithm:

* Comb Sort, descending by `rating`.

Why Comb Sort was selected:

* It is different from insertion sort.
* It is simple to implement from scratch.
* It can sort custom dictionaries using a comparison key.
* It is easy to explain in checkoff.

## 9. Exercise 3 UI Design Explanation

How users input data:

* Idea name with `text_input`.
* Category with `text_input`.
* Rating with a slider from `0.5` to `5.0`, stepping by `0.5`.

Star preview:

* The slider value is converted by `rating_to_stars()`.
* Full stars use `★`.
* Half stars use `½`.
* Empty stars use `☆`.
* Example: `4.5` displays as `★★★★½`.
* Example: `3.0` displays as `★★★☆☆`.
* Example: `2.5` displays as `★★½☆☆`.

How users trigger sorting:

* Click `Sort by Rating`.

How users reset:

* Click `Reset`.

How results display:

* `Original Ideas` table shows the current idea list.
* `Sorted Ideas` table shows ideas ordered from highest rating to lowest rating.

### UI Iteration 1: Basic Dropdown/Slider Rating

* Show sample project ideas in one table.
* Use a basic numeric slider or dropdown for rating.
* Provide `Add Idea`, `Sort by Rating`, and `Reset`.
* Sorted ideas appear below.

Pros:

* Simple to build.
* Meets the functional requirement.

Cons:

* Numeric ratings alone are less visual.
* The user experience feels less like a real rating system.

### UI Iteration 2: Star Rating Visual System with Half-Star Support

* Use a slider from `0.5` to `5.0`.
* Show a large star preview below the slider.
* Support full stars, half stars, and empty stars.
* Keep original and sorted tables clearly separated.

Final choice:

* The final app uses the star rating visual system because it is more intuitive, more realistic, and easier to explain during the demo.

## 10. Brainstorming for Exercise 3 Data

| Idea | Data sorted | Real app context | Fit | Complexity |
|---|---|---|---|---|
| Project Idea Ranker | Ideas by star rating | Hackathons, class projects | Strong | Low |
| Email inbox sorter | Emails by importance | Gmail, Outlook | Good | Medium |
| Playlist sorter | Songs by genre/rating | Music apps | Good | Medium |
| Event sorter | Events by urgency | Calendar apps | Good | Medium |
| Contact sorter | Contacts by group | Contacts/CRM | Good | Low |
| Support ticket sorter | Tickets by severity | Helpdesk systems | Strong | Medium |

## 11. Pugh Chart for Choosing Data Idea

Baseline: Project Idea Ranker.

| Criteria | Project Ideas | Email Inbox | Playlist | Contact List | Support Tickets |
|---|---:|---:|---:|---:|---:|
| Fits non-numeric records | 0 | 0 | 0 | 0 | 0 |
| Easy Streamlit input | 0 | - | - | 0 | - |
| Easy to explain | 0 | - | 0 | 0 | - |
| Real-world relevance | 0 | + | + | 0 | + |
| Good visual display | 0 | 0 | + | 0 | 0 |
| Low implementation risk | 0 | - | - | 0 | - |

Final choice:

* Project Idea Ranker is realistic, simple to input, and clearly demonstrates sorting records by one field.

## 12. Brainstorming for Sorting Algorithm

| Algorithm | Basic idea | Pros | Cons | Fits our data? | Difficulty |
|---|---|---|---|---|---|
| Comb Sort | Compare items with shrinking gap | Simple, different from insertion sort | Worst case `O(n^2)` | Yes | Easy-medium |
| Merge Sort | Split, sort, merge | Reliable `O(n log n)` | More recursive code | Yes | Medium |
| Quick Sort | Pick pivot and partition | Fast average case | Pivot explanation can be tricky | Yes | Medium |
| Heap Sort | Use a heap | Good complexity | Harder to explain | Yes | Hard |
| Counting/Radix | Count or process digits | Fast for limited keys | Less natural for records | Maybe | Medium |

Needs confirmation:

* Confirm Comb Sort was not taught in class, cohort problem set, or homework.

## 13. Pugh Chart for Choosing Algorithm

Baseline: Comb Sort.

| Criteria | Comb Sort | Merge Sort | Quick Sort | Heap Sort | Counting/Radix |
|---|---:|---:|---:|---:|---:|
| Not taught in class | 0 | 0 | 0 | 0 | 0 |
| Implemented from scratch | 0 | 0 | 0 | - | 0 |
| Works with dictionaries | 0 | 0 | 0 | 0 | - |
| Easy whiteboard explanation | 0 | - | - | - | - |
| Reliable for small app | 0 | + | 0 | + | - |
| Reasonable code complexity | 0 | - | 0 | - | - |

Why Comb Sort was selected:

* It is easy to explain.
* It is visibly different from insertion sort.
* It works with project idea dictionaries by comparing the rating field.

## 14. Code Quality Explanation

* Shared logic is in `library.py`.
* Streamlit pages call reusable functions.
* Built-in sorting functions are avoided.
* Exercise 2 handles invalid input.
* Exercise 3 uses clear session state keys for ideas and sorted ideas.
* The app can be tested with pytest.
* The app can be run with `streamlit run Home.py`.

Possible improvements:

* Add edit/delete for project ideas.
* Add more tests for empty idea lists and tied ratings.
* Confirm the special random seed behavior.

## 15. User Experience Explanation

* Clear page titles.
* Buttons use obvious labels.
* Exercise 3 uses a familiar star rating preview.
* Half-star support makes ratings feel more realistic.
* Original and sorted lists are shown in tables.
* Reset lets users restart without refreshing.

## 16. Demo Script

### Speaker 1: Overview and file structure

Our project is a Streamlit Sorting App. The main file is `Home.py`, shared functions are in `library.py`, and exercise pages are in the `pages` folder. The README goals are to build a simple Streamlit app, use widgets, and display data.

### Speaker 2: Exercise 1

Exercise 1 generates 10 random numbers using a timestamp seed. The Generate button stores the numbers in session state. The Sort button converts them back to integers, uses insertion sort through `my_sort()`, and displays the sorted result.

### Speaker 3: Exercise 2

Exercise 2 lets users type comma-separated numbers. The app splits the string, converts values to integers, sorts them, and displays the result. It also has a Clear button and invalid input handling.

### Speaker 4: Exercise 3

Exercise 3 is a Project Idea Ranker. Users add an idea name, category, and rating from 0.5 to 5.0. The slider shows a star preview with full stars, half stars, and empty stars. The app sorts project idea records by rating from highest to lowest using Comb Sort. This satisfies the non-numeric data requirement because we sort dictionaries, not plain numbers.

### Speaker 5: Design decisions

We chose Project Idea Ranker because it is realistic and easy to demo. We chose Comb Sort because it is not insertion sort, can be implemented from scratch, and is easy to whiteboard. The final UI uses the star rating visual system because it is intuitive and realistic.

## 17. Quick 2-Minute Version

This Streamlit app demonstrates sorting through three exercises. Exercise 1 generates random numbers and sorts them. Exercise 2 sorts user-entered comma-separated numbers. Both use `my_sort()`, which implements insertion sort.

Exercise 3 is a Project Idea Ranker. Each idea has an idea name, category, and rating from 0.5 to 5.0. The app sorts the list of idea dictionaries by rating from highest to lowest using Comb Sort from scratch. It satisfies the non-numeric requirement because the data being sorted is a project idea record, and the rating is only one field inside that record.

## 18. Likely Instructor Questions and Answers

| Question | Answer |
|---|---|
| Why Streamlit? | It is required and makes widgets easy in Python. |
| What is session state? | Storage that keeps values after Streamlit reruns. |
| Why not use `sorted()`? | The assignment requires custom sorting algorithms. |
| How does Exercise 3 satisfy non-numeric data? | It sorts idea dictionaries with text fields and a rating field, not plain numbers. |
| How does Comb Sort work? | It compares items separated by a shrinking gap and swaps them when needed. |
| Why choose Comb Sort? | It is different from insertion sort, simple to implement, and easy to explain. |
| Why use a star preview? | It makes the rating input feel like a real ranking app and supports half-star ratings. |
| What happens with invalid Exercise 2 input? | The app shows an error instead of crashing. |
| What would you improve? | Add idea editing/deleting and more tests. |

## 19. Whiteboard Coding Prep

### my_sort(): Insertion Sort

```text
for each index from 1 to end:
    key = current item
    move larger previous items right
    insert key into correct place
```

### comb_sort_ideas(): Comb Sort

```text
function comb_sort_ideas(ideas):
    pair each idea with its original index
    gap = length of list
    swapped = true

    while gap > 1 or swapped:
        shrink gap by dividing by 1.3
        if gap < 1, set gap to 1

        swapped = false
        for each idea i with comparison idea j = i + gap:
            if idea i has lower rating than idea j:
                swap them
                swapped = true

    return ideas without original indexes
```

Example:

```text
Idea A rating 3.5
Idea B rating 5.0
Idea C rating 4.5

Sorted:
Idea B rating 5.0
Idea C rating 4.5
Idea A rating 3.5
```

## 20. Testing and Running Instructions

```shell
python -m pipenv install
python -m pipenv run pytest
python -m pipenv run streamlit run Home.py
```

Manual browser checks:

* Exercise 1 generates and sorts numbers.
* Exercise 2 sorts user input.
* Exercise 2 clears input and output.
* Exercise 3 adds a project idea.
* Exercise 3 shows full, half, and empty star previews.
* Exercise 3 sorts ideas by rating from highest to lowest.
* Exercise 3 reset works.

## 21. Submission Checklist

* [ ] `pytest` passes.
* [ ] Streamlit app runs.
* [ ] Exercise 1 works.
* [ ] Exercise 2 works.
* [ ] Exercise 3 Project Idea Ranker works.
* [x] `docs/TEAM_PRESENTATION_BRIEF.md` created.
* [ ] Miro/Figma UI iterations prepared.
* [x] Data brainstorming prepared.
* [x] Data Pugh Chart prepared.
* [x] Algorithm brainstorming prepared.
* [x] Algorithm Pugh Chart prepared.
* [ ] Git add/commit/push completed.
* [ ] Gradescope/eDimension submission completed.
