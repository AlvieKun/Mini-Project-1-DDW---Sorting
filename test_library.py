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
        {"idea": "Campus Food Finder", "category": "Student Life", "rating": 3.5},
        {"idea": "Accessibility Route Planner", "category": "Social Impact", "rating": 5.0},
        {"idea": "AI Study Planner", "category": "Education", "rating": 4.5},
        {"idea": "Roommate Chore App", "category": "Home", "rating": 5.0},
    ]
    output = comb_sort_ideas(ideas)
    assert output == [
        {"idea": "Accessibility Route Planner", "category": "Social Impact", "rating": 5.0},
        {"idea": "Roommate Chore App", "category": "Home", "rating": 5.0},
        {"idea": "AI Study Planner", "category": "Education", "rating": 4.5},
        {"idea": "Campus Food Finder", "category": "Student Life", "rating": 3.5},
    ]
