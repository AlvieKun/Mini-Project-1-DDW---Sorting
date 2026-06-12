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

def sample_ideas():
    return [
        {
            "idea": "Campus Food Finder",
            "category": "Student Life",
            "score": 3.5,
            "description": "",
        },
        {
            "idea": "accessibility Route Planner",
            "category": "Social Impact",
            "score": 5.0,
            "description": "",
        },
        {
            "idea": "AI Study Planner",
            "category": "Education",
            "score": 4.5,
            "description": "",
        },
        {
            "idea": "Smart Recycling Bin",
            "category": "Sustainability",
            "score": 4.0,
            "description": "",
        },
    ]


def test_comb_sort_ideas_alphabetical():
    output = comb_sort_ideas(sample_ideas(), "alphabetical")
    assert [idea["idea"] for idea in output] == [
        "accessibility Route Planner",
        "AI Study Planner",
        "Campus Food Finder",
        "Smart Recycling Bin",
    ]


def test_comb_sort_ideas_score_high():
    output = comb_sort_ideas(sample_ideas(), "score_high")
    assert [(idea["idea"], idea["score"]) for idea in output] == [
        ("accessibility Route Planner", 5.0),
        ("AI Study Planner", 4.5),
        ("Smart Recycling Bin", 4.0),
        ("Campus Food Finder", 3.5),
    ]


def test_comb_sort_ideas_score_low():
    output = comb_sort_ideas(sample_ideas(), "score_low")
    assert [(idea["idea"], idea["score"]) for idea in output] == [
        ("Campus Food Finder", 3.5),
        ("Smart Recycling Bin", 4.0),
        ("AI Study Planner", 4.5),
        ("accessibility Route Planner", 5.0),
    ]


def test_comb_sort_ideas_tie_preservation():
    ideas = [
        {"idea": "  Banana", "category": "First", "score": 4.0, "description": ""},
        {"idea": "banana", "category": "Second", "score": 4.0, "description": ""},
        {"idea": "Apple", "category": "Third", "score": 5.0, "description": ""},
    ]
    output = comb_sort_ideas(ideas, "alphabetical_then_score")
    assert [idea["idea"] for idea in output] == [
        "Apple",
        "  Banana",
        "banana",
    ]
    assert output[1]["category"] == "First"
    assert output[2]["category"] == "Second"
