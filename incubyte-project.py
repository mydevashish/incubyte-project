def add(numbers: str) -> int:
    if not numbers:
        return 0
    return int(numbers)

def test_single_number():
    assert add("1") == 1

if __name__ == "__main__":
    test_single_number()