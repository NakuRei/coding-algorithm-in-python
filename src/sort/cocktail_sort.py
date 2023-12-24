from pkg import timer


def swap_forward(numbers: list[int], idx_start: int, idx_end: int) -> bool:
    is_swapped = False
    for i in range(idx_start, idx_end):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            is_swapped = True
    return is_swapped


def swap_backward(numbers: list[int], idx_start: int, idx_end: int) -> bool:
    is_swapped = False
    for i in range(idx_end, idx_start, -1):
        if numbers[i - 1] > numbers[i]:
            numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
            is_swapped = True
    return is_swapped


@timer
def cocktail_sort(numbers: list[int]) -> list[int]:
    idx_start = 0
    idx_end = len(numbers) - 1

    while True:
        if not swap_forward(numbers, idx_start, idx_end):
            break
        idx_end -= 1

        if not swap_backward(numbers, idx_start, idx_end):
            break
        idx_start += 1

    return numbers


if __name__ == "__main__":
    import random

    orig_numbers = [random.randint(0, 1000) for _ in range(100)]
    sorted_numbers = cocktail_sort(orig_numbers.copy())

    print(f"original numbers: {orig_numbers}")
    print(f"sorted numbers: {sorted_numbers}")
