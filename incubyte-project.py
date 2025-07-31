def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = numbers.split(",")
    return sum(int(p) for p in parts)

def test_multiple_numbers_return_sum():
    print(add("1,2,3,4") == 10)
    assert add("1,2,3,4") == 10

if __name__ == "__main__":
    test_multiple_numbers_return_sum()