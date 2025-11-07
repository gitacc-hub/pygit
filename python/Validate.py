while True:
    age = input("Enter your age (or 'q' to quit): ")

    if age.lower() == 'q':
        break

    if not age.isdigit():
        print("Age can only be a number.")
        continue

    age = int(age)

    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You are an adult.")
    else:
        print("You are a young person.")

print("Thanks for participating.")

