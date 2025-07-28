# Prompt User for a Number
try:
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and Print the Multiplication Table
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    print("Invalid input. Please enter an integer number.")
