# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
"""Example:

for i in FibonacciNumbers(10):
    print(i)
0
1
1
2
3
5
8
13
21
34
55
"""

print("Task #1")


class FibonacciNumbers:
    first_number = 0
    second_number = 1
    count = 0

    def __init__(self, number_of_values: int):
        self.number_of_values = number_of_values

    def __iter__(self):

        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.first_number
        if self.count == 1:
            self.count += 1
            return self.second_number
        if self.count < self.number_of_values:
            self.count += 1
            num_fibonacci = self.first_number + self.second_number
            self.first_number = self.second_number
            self.second_number = num_fibonacci
            return num_fibonacci
        else:
            raise StopIteration


result = []
for i in FibonacciNumbers(10):
    result.append(i)

print(result)

# 2.* Implement generator for Fibonacci numbers
print("Task #2")

class FibonacciNumbers:
    x = 0
    x1 = 1


# 3. Write generator expression that returns square numbers of integers from 0 to 10
print("Task #3")

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
print("Task #4")

# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
print("Task #5")
