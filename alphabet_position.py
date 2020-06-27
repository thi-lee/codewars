# my solution
def alphabet_position(text):
    str2 = ""
    for letter in text.lower():
        if ord(letter) not in range(97, 123): # check if it's alphabet
            continue
        str2 += str((ord(letter) - ord('a') + 1)) + " "

    return(str2.strip())

# best practice
'''
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
'''

'''
There are controversies about whether isalpha() is the best practice here,
but I think this solution still show how useful join() turns out to be
'''

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
