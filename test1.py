from setuptools.command.easy_install import is_python


def is_palindrome(string):
    reversed_String = string[::-1]
    print(reversed_String)
    if string == reversed_String:
        return True
    else:
        return False


myString = "malayalam"
print(is_palindrome(myString))