from pathlib import Path
from icecream import ic
import re

def read_input(filepath: Path) -> str:
    with open(filepath, "r") as file:
        text = file.readlines()
    return text


input = read_input(Path(__file__).parent / "input.txt")

# ic(len(input))
def get_matches(string: str, pattern: str=r'mul\(\d{1,3}\,\d{1,3}\)'):
    return re.findall(
        pattern=pattern,
        string=string
    )

def extract_numbers(string: str) -> list[int, int]:
    substrings = re.split(r'\,', string)
    return [int(re.findall(r'\d+', num)[0]) for num in substrings]


def part_1():
    total = 0
    for line in input:
        matches = get_matches(line)
        total += sum_multiples(matches)

    return total

def sum_multiples(matches):
    return sum([num[0] * num[1] for num in [extract_numbers(string) for string in matches]])

def get_matches_dos_and_donts() -> list[str]:
    matches = []
    for line in input:
        matches += get_matches(line, pattern=r'mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)')
    
    return matches

def part_2():
    included = []
    state = True
    for match in get_matches_dos_and_donts():
        if match == "do()":
            state = True
        elif match == "don't()":
            state = False
        else:
            if state:
                included.append(match)

    return sum_multiples(included)


ic(part_1())
ic(part_2())
