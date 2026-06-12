from library import gen_random_int, my_sort, create_string, comb_sort_ideas
import pytest

def test_gen_random_int():
    output = gen_random_int(10, 100)
    assert output == [4, 0, 5, 9, 3, 1, 6, 8, 7, 2]

def test_my_sort():
    array = [10.3,3.8,8.4,47.1,1.0,0,-39.8,8.4,4.7,7.6,-6.5,-5.0]
    my_sort(array)
    assert array == [-39.8, -6.5, -5.0, 0.0, 1.0, 3.8, 4.7, 7.6, 8.4, 8.4, 10.3, 47.1]

def test_create_string():
    array = [4, 0, 5, 9, 3, 1, 6, 8, 7, 2]
    output = create_string(array)
    assert output == "4, 0, 5, 9, 3, 1, 6, 8, 7, 2."

def test_comb_sort_ideas():
    ideas = [
        {"idea": "Campus Food Finder", "category": "Student Life", "description": ""},
        {"idea": "accessibility Route Planner", "category": "Social Impact", "description": ""},
        {"idea": "AI Study Planner", "category": "Education", "description": ""},
        {"idea": "Smart Recycling Bin", "category": "Sustainability", "description": ""},
        {"idea": "ai study planner", "category": "Duplicate", "description": "same idea name"},
    ]
    output = comb_sort_ideas(ideas)
    assert [idea["idea"] for idea in output] == [
        "accessibility Route Planner",
        "AI Study Planner",
        "ai study planner",
        "Campus Food Finder",
        "Smart Recycling Bin",
    ]
    assert output[1]["category"] == "Education"
    assert output[2]["category"] == "Duplicate"
