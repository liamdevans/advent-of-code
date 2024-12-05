from pathlib import Path
from icecream import ic

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as file:
        text = file.readlines()
    return text

def split_input_into_lists(input: list):
    list_a = []
    list_b = []
    for line in input:
        num1, num2 = line.split()
        list_a.append(int(num1))
        list_b.append(int(num2))
    return list_a, list_b
                    

def problem_1():
    input = read_input(Path(__file__).parent / "input.txt")
    list_a, list_b = split_input_into_lists(input)

    combined = list(zip(sorted(list_a), sorted(list_b)))

    total = 0
    for item_a, item_b in combined:
        total += abs(item_a - item_b)

    ic(total)


def problem_2():
    input = read_input(Path(__file__).parent / "input.txt")
    list_a, list_b = split_input_into_lists(input)

    similarity_score = 0
    for number in list_a:
        similarity_score += number * list_b.count(number)

    ic(similarity_score)


if __name__ == "__main__":
    problem_1()
    problem_2()