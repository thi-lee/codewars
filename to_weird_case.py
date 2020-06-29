# Instructions:
# Write a function that accepts a string
# and returns the same string with all
# the even indexed characters of each
# word upper cased. The indexing is zero-based.

# my solution (definitely nowhere close to the best solution)

def to_weird_case(string):
    str2 = string.split()
    str3 = []
    str4 = []
    for i in range(len(str2)):
        lst = list(enumerate(str2[i]))
        for tup in lst:
            (index, letter) = tup
            if index % 2 == 0:
                str3.append(letter.capitalize())
            else:
                str3.append(letter)
        str4.append(''.join(str3))
        str3 = []
    return(' '.join(str4))

# I learned how to use enumerate()
# challenges in this kata: dealing w words
# with repeated letters

# clever:
'''
def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))

def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())
'''

print(to_weird_case('This is a test'))
print(to_weird_case('Looks like you passed'))
print(to_weird_case('This is the final test case'))
print(to_weird_case('Just kidding'))
print(to_weird_case('Ok fine you are done now'))
