from pkg import timer
import random


def is_sorted(numbers: list[int]) -> bool:
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


@timer
def bogo_sort(numbers: list[int]) -> list[int]:
    while not is_sorted(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    orig_numbers = [random.randint(0, 100) for _ in range(10)]
    sorted_numbers = bogo_sort(orig_numbers.copy())

    print(f"original numbers: {orig_numbers}")
    print(f"sorted numbers: {sorted_numbers}")
