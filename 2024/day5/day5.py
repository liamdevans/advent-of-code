from pathlib import Path
from icecream import ic
from collections import deque

def read_input(filepath: Path) -> tuple[list[deque], list[deque]]:
    with open(filepath, "r") as file:
        orders = []
        updates = []
        second = False
        for line in file.readlines():
            if line == "\n":
                second = True
                continue
            if second:
                updates.append(deque([int(num) for num in line.split(",")]))
            else:
                orders.append(deque([int(num) for num in line.split("|")]))
    return orders, updates

ORDERS, UPDATES = read_input(Path(__file__).parent / "input.txt")

def get_orderd_dict():
    """Create dict with BEFORE as key and AFTER as values."""
    order_dict = {}
    for before, after in ORDERS:
        order_dict.setdefault(before, set()).add(after)
    return order_dict

ORDERS_DICT = get_orderd_dict()

def is_ordered(update: deque[int]) -> bool:
    """Check if starting num exists in 'after' list of other nums. If not continue to next."""
    size = len(update)
    update_ = update.copy()
    for _ in range(size):
        num_to_check = update_.popleft()
        for num in update_:
            if num_to_check in ORDERS_DICT[num]:
                return False
    return True

def get_sorted_updates(unsorted: bool = False):
    """Filter through updates and return only sorted."""
    updates = []
    for update in UPDATES:
        if unsorted:
            if not is_ordered(update):
                updates.append(update)
        else:
            if is_ordered(update):
                updates.append(update)
    return updates

def get_middle_of_deque(update: deque[int]) -> int:
    """Return value at middle index. Assumes odd number of items."""
    size = len(update)
    middle_idx = int((size - 1) / 2)
    return update[middle_idx]

def part_1():
    return sum([get_middle_of_deque(update) for update in get_sorted_updates()])

def sort_update(update: deque[int]) -> deque[int]:
    """Given an update, will return sorted version."""
    size = len(update)
    original_update = update.copy()
    new_update = deque()
    for idx in range(size):
        num_to_check = original_update.popleft()
        for num in original_update:
            if num_to_check in ORDERS_DICT[num]:
                new_update.append(num) # SWAP items with issues
                new_update.append(num_to_check)
                new_update.extend(item for item in original_update if item != num)
                return sort_update(new_update)
        new_update.append(num_to_check)
    return new_update


def part_2():
    force_sorted_updates = [sort_update(update) for update in get_sorted_updates(unsorted=True)]
    return sum([get_middle_of_deque(update) for update in force_sorted_updates])

ic(part_1())
ic(part_2())
