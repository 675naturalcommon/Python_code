def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    first_name = input("Enter your first name: ")
    if first_name == "quit":
        break
    last_name = input("Enter your last name: ")
    if last_name == "quit":
        break
    formatted_name = format_name(first_name, last_name)
    print(f"Hello, {formatted_name}!")