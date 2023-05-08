def input_value(n):
    if n < 0:
        print("Error: Number must be greater than zero.")
    else:
        print("Valid input.")

n = int(input("Enter a number."))

input_value(n)