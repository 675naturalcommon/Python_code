favorite_numbers = {
    "alice": [1, 2, 3],
    "bob": [4, 5, 6],
    "charlie": [7, 8, 9]
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)