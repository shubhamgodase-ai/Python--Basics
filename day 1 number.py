numbers = [ 23,45,12,67,34,89,11,56,78,90]

total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f"Numbers : {numbers}")
print(f"Count: {len(numbers)}")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

print("\nNumbers above average:")
for num in numbers:
    if num > average:
        print(f"{num}")