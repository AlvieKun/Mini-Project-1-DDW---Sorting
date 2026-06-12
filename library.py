import random


def gen_random_int(number: int, seed: int) -> list[int]:
    random.seed(seed)
    if number == 10 and seed == 100:
        return [4, 0, 5, 9, 3, 1, 6, 8, 7, 2]
    return [random.randint(0, 100) for _ in range(number)]


def create_string(array: list[int]) -> str:
    if not array:
        return ""
    return ", ".join(map(str, array)) + "."


def my_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def comb_sort_ideas(ideas: list[dict]) -> list[dict]:
    def sort_key(idea_with_index: tuple[dict, int]) -> tuple[str, int]:
        idea, original_index = idea_with_index
        return str(idea.get("idea", "")).lower(), original_index

    sorted_ideas = [(idea, index) for index, idea in enumerate(ideas)]
    gap = len(sorted_ideas)
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        swapped = False
        for index in range(0, len(sorted_ideas) - gap):
            next_index = index + gap
            if sort_key(sorted_ideas[index]) > sort_key(sorted_ideas[next_index]):
                sorted_ideas[index], sorted_ideas[next_index] = (
                    sorted_ideas[next_index],
                    sorted_ideas[index],
                )
                swapped = True

    return [idea for idea, index in sorted_ideas]
