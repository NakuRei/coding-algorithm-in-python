from pkg import timer


@timer
def bubble_sort(numbers: list[int]) -> list[int]:
    for limit_idx in range(len(numbers), 1, -1):
        for i in range(1, limit_idx):
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
    return numbers


if __name__ == "__main__":
    import random

    orig_numbers = [random.randint(0, 1000) for _ in range(100)]
    sorted_numbers = bubble_sort(orig_numbers.copy())

    print(f"original numbers: {orig_numbers}")
    print(f"sorted numbers: {sorted_numbers}")
