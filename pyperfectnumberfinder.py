def find_perfect_numbers(upper_limit):
    perfect_numbers = []
    for number in range(1, upper_limit + 1):
        divisors = []
        for i in range(1, number):
            if number % i == 0:
                divisors.append(i)
        if sum(divisors) == number:
            perfect_numbers.append(number)
    return perfect_numbers

upper_limit = int(input("Enter the upper limit: "))
perfect_numbers = find_perfect_numbers(upper_limit)

print(f"Perfect numbers up to {upper_limit}: {perfect_numbers}")
