#!/usr/bin/env python3
#!/usr/bin/env python3

# prompt the user for their position
position = int(input("Please enter a position in the Fibonacci sequence: "))

# initialize 2 integers
a, b = 0, 1

for i in range(position):
    a, b = b, a + b

fibonacci_number = a

print(f"The Fibonacci number for {position} is {fibonacci_number}")

