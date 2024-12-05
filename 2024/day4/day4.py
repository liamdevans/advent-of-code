from pathlib import Path
from icecream import ic
from dataclasses import dataclass

def apply_grid(filepath: Path) -> list[list[str]]:
    with open(filepath, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def word_search(
        grid: list[list[str]], 
        word: str,
        return_positions: bool = False,
) -> int:
    count = 0
    positions: list[Position] = []

    for r_idx, row in enumerate(grid):
        for c_idx, column in enumerate(row):
            if grid[r_idx][c_idx] == word[0]: # start search at first letter of word
                match_count, match_positions = search_directions(grid, r_idx, c_idx, word)
                count += match_count
                positions += match_positions

    if return_positions:
        return count, positions
    return count
            
def search_directions(
        grid: list[list[str]], 
        r_idx: int, 
        c_idx: int, 
        word: str,
        directions: list[tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)],
) -> int:
    count = 0
    positions: list[Position] = []

    for dr, dc in directions:
        cur_row = r_idx
        cur_col = c_idx

        word_match_so_far = ""
        for letter in word:
            if cur_row < 0 or cur_col < 0 or cur_row >= len(grid) or cur_col >= len(grid[0]) or grid[cur_row][cur_col] != letter:
                break

            word_match_so_far += letter
            if word_match_so_far == word:
                count += 1
                start_coord = Coords(r_idx, c_idx)
                end_coords = Coords(cur_row, cur_col)
                positions.append(Position(start_coord, end_coords))

            cur_row += dr
            cur_col += dc

    return count, positions

grid = apply_grid(Path(__file__).parent / "input.txt")

def part_1():
    return word_search(grid, "XMAS")


@dataclass(order=True)
class Coords:
    row: int
    col: int

    # def __add__(self, other): 
    #     if not isinstance(other, Coords): 
    #         return NotImplemented 
    #     return Coords(self.row + other.row, self.col + other.col) 
    
    # def __sub__(self, other): 
    #     if not isinstance(other, Coords): 
    #         return NotImplemented 
    #     return Coords(self.row - other.row, self.col - other.col)
    
    def combine(self, other):
        if not isinstance(other, Coords): 
            return NotImplemented 
        return [Coords(self.row, other.col), Coords(other.row, self.col)]

@dataclass
class Position:
    starting: Coords
    ending: Coords

    def __eq__(self, other): 
        if not isinstance(other, Position): 
            return NotImplemented 
        return ((self.starting == other.starting and self.ending == other.ending) or
                 (self.starting == other.ending and self.ending == other.starting))
    
    def is_diagonal(self):
        return self.starting.row != self.ending.row and self.starting.col != self.ending.col


def cross_position(match: Position) -> Position:
    """Given Position of a word, possible Positions of a potential cross.
    """
    new_start, new_end = match.starting.combine(match.ending)
    return Position(new_start, new_end)



def part_2():
    word = "MAS"
    _, matched_words_pos = word_search(grid, word, return_positions=True)
    count = 0

    for position in matched_words_pos:
        if position.is_diagonal():
            if cross_position(position) in matched_words_pos:
                count += 1
    return count / 2


# ic(part_1())
ic(part_2())

# _, matched_words_pos = word_search(grid, "MAS", return_positions=True)
# ic(matched_words_pos)

# ic(grid[139][123], grid[139][121])