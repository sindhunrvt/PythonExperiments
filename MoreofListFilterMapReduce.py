#Given a list of numbers, use list comprehension to create a new list containing the squares of only the even numbers.
import math

inputList = [3,6,7,23,45,65,34,82, 19,12, 26]
print( [x**2 for x in inputList if x%2 == 0])

#Extract Vowels from a String -Given a string, use list comprehension to extract all vowels (a, e, i, o, u).
sentence = "This is my home"
vowels = ['a', 'e', 'i', 'o', 'u']
print([ch for ch in sentence.lower() if ch in vowels])

#Given a list of numeric strings, use list comprehension to convert them into integers.
data = ["1", "2", "3"]
print([int(x) for x in data])

#Given a number n, generate a list of the first 10 multiples of n using list comprehension.
n = int(input("Enter a number: "))
print([n*x for x in range (1, 11)])

#Given a list of numbers, use filter() to return only prime numbers.
inputList = [3,6,7,23,45,65,34,82, 19,12, 26,11,23,43,47]
def checkprime(x):
    if x <= 0: return False
    return all(x%i!=0 for i in range (2, int(math.sqrt(x))+1))
print(list(filter(checkprime , inputList)))

#Given a list of strings, use filter() to remove all empty strings ("").
list_of_strings = ["abc", "", " abc", "def", "", "tru l"]
print(list(filter(lambda x: x != "", list_of_strings)))

#Given a list of words, use filter() to return only those that are longer than 5 characters.
list_of_strings = ["abc", "", " abc", "def", "", "tru l123", "werty", "t6y7u8"]
print(list(filter(lambda x: len(x) > 5, list_of_strings)))

#Given a list of words, use filter() to extract only palindromes (words that read the same forward and backward).
list_of_words = ["madam", "hello", "racecar", "world"]
print(list(filter(lambda x: x == x[::-1], list_of_words)))

#Given a list of numbers, use map() to double each element.
list_of_numbers = [3, 6,7,9,10]
print(list(map(lambda x:x *2 ,list_of_numbers)))

#Given a list of temperatures in Fahrenheit, use map() to convert them to Celsius.
list_of_numbers = [80, 56, 78, 32]
print(list(map(lambda F: round( (F - 32) * 5/9, 2) ,list_of_numbers)))

#Given a list of words, use map() to capitalize the first letter of each word.
list_of_words = ["madam", "hello", "racecar", "world"]
print(list(map(lambda x : x.capitalize(), list_of_words)))

#Given a list of words, use map() to return a list of their lengths.
print(list(map(lambda x : len(x), list_of_words)))

#Given a list of numbers, use reduce() to find the maximum number.
from functools import reduce
numbers = [10, 45, 78, 23, 89, 67, 91, 34]
print(reduce(lambda x,y: x if x>y else y, numbers))

#Given a list of numbers, use reduce() to compute the product of all elements.
numbers = [2,4,6,7]
print(reduce(lambda x,y: x*y, numbers))

#Given a list of strings, use reduce() to concatenate them into a single string.
strings = ["This", "is", "a", "string"]
print(reduce(lambda x,y: x+' '+y, strings))
#Given a list of words, use reduce() to find the longest word.
print(reduce(lambda x,y: x if len(x) > len(y) else y, strings))
