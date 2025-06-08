# Write a function that computes the# sum and average of a list of numbers

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def calculate_average(numbers):
    if not numbers:
        return 0
    total = calculate_sum(numbers)
    avg = total / len(numbers)
    return avg

user_input = input("Enter Numbers with Commas: ")

list_of_numbers = list(map(float, user_input.replace(","," ").split()))

sum_of_numbers = calculate_sum(list_of_numbers)
average_of_numbers = calculate_average(list_of_numbers)

print("sum: ", sum_of_numbers)
print("Average: ", average_of_numbers)