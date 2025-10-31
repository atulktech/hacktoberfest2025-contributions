def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        even_sum += num * (num % 2 == 0)
        odd_sum += num * (num % 2 == 1)

    return even_sum, odd_sum

numbers = [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 14]
even, odd = sum_even_odd(numbers)

print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
