students = {
    "Alice": 85,
    "Bob": 48,
    "Charlie": 93,
    "Diana": 55
}

name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Student '{name}' not found.")
