#Patrick McCormack

def sum_of_squares(numbers):
    """
    Given a list of integers, return the sum of the squares of the integers.
    """
    return sum(x ** 2 for x in numbers)


def count_strings(*strings):  # had to look up the code for count_strings to call multiple arguments
    """
    Given any number of string arguments, return the number of strings provided.
    """
    return len(strings)


print("Counting the sum of squares ")
print(sum_of_squares([1, 2, 3]))  
print(sum_of_squares([4, 5, 6]))  
print(sum_of_squares([7, 8, 9]))  


print("Counting the strings ")
print(count_strings("hello", "world")) 
print(count_strings("python", "is", "fun"))  
print(count_strings("a", "b", "c", "d", "e"))  