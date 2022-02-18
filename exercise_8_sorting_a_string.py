"""
In this exercise you'll write a function, strsort, that takes a single string
as its inupt and returns a string. The returned string should contain the same
characters as the input, except that its characters should be stored in order,
from the lowes Unicode value to the highest Unicode value. For example, the
result of invoking strsort('cba') will be string abc.
"""

# my solution
def strsort(strg: str) -> str:
    return ''.join(sorted([letter for letter in strg]))


print(strsort('cba'))

# solution from the book
def strsort(a_string):
    return ''.join(sorted(a_string))

# Am I overusing list comperhensions? :)

# Beyond exercise
"""
Consider a few other varaitions of, and extentions to, this exercise which also
use str.split and str.join as well as sored:
- given string 'Tom Dick Harry' break it into infividual words, and then sort those words alphabetically. 
Once they're sorted, print them with commas (,) between the names 
"""
def str_sort(b_string: str) -> str:
    return ', '.join(sorted(b_string.split()))

print(str_sort('Tom Dick Harry'))
