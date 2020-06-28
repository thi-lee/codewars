# my solution:
def countBits(n):
    return sum([int(i) for i in f'{n:08b}'])
# not gonna lie, I'm pretty impressed with myself :)
# I looked through other solutions, and I wonder whether
# it's better to use built-in or come up with a solution
# using what I already know/reinventing what's already there
# This code of mine isn't the best out there, but compared
# days before I have gotten better.

# Here's a solution rated best practice:
'''
def countBits(n):
    return bin(n).count("1")
'''


print(countBits(0))
print(countBits(4))
print(countBits(7))
print(countBits(9))
print(countBits(10))
print(countBits(26))
print(countBits(77231418))
print(countBits(12525589))
print(countBits(3811))
print(countBits(392902058))
print(countBits(1044))
print(countBits(10030245))
