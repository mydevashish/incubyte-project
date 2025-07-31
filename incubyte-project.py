def add(numbers: str) -> int:
    if not numbers:
        return 0
    return int(numbers)

def test_two_numbers():
    print(add("1,2") == 3)
    assert add("1,2") == 3

if __name__ == "__main__":
    test_two_numbers()