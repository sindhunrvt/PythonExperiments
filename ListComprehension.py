from curses.ascii import isdigit

inputList = [23,56,78,35,66,98,9,78,45,68,91]

print([x for x in inputList if x%2 == 0])
print(list(filter(lambda x: x%2 == 0 , inputList)))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([num for row in matrix  for num in row if num%2 == 0])
print([num for row in matrix for num in row if num%2 !=0])

words = ["sky", "apple", "rhythm", "orange", "crypt"]
def has_vowel(word):
    vowels = ['a','e','i','o','u']
    return any(char in vowels for char in word.lower())

print(list(filter(has_vowel, words)))
nested_list = [[1, -2, 3], [-4, 5, -6], [7, 8, -9]]
print([num for row in nested_list for num in row if num > 0])

from itertools import chain
print([x for x in list(chain(*nested_list)) if x<0])

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

import math
def is_prime(n):
    return n>1 and all ( n%i != 0 for i in range (2, int(math.sqrt(n))+1))
print([x for x in range (2, 101) if is_prime(x) ])

def checkpalindrome(word):
    return word == word[::-1]

words = ["radar", "hello", "level", "world", "madam"]
print([word for word in words if checkpalindrome(word)])


words = ["banana", "apple", "kiwi", "strawberry", "grape"]
print(list(filter(lambda word: (len(word)> 5), words)))

def fibonacci(n):
    fib = [0,1]
    [fib.append(fib[-1]+fib[-2]) for _ in range(n-2)]
    return fib

#print([fibonacci(x) for x in range(10)])

n = 10
print(fibonacci(n))

text = "Hello123World45"

print([ch for ch in text if ch.isdigit()])

data = [("a", 5), ("b", 15), ("c", 8), ("d", 20)]
print({x:y for x,y in data if y > 10})


sentence = "This is a sample sentence for testing"



stopwords = ["is", "a", "for"]
print([ word for word in sentence.lower().split(' ') if word not in stopwords])