# my solution:
def high_and_low(numbers):
    num = numbers.split()
    lst = []
    num = list(map(int, num))
    lst.append(sorted(num, reverse=True)[0])
    lst.append(sorted(num, reverse=True)[-1])
    return ' '.join(list(map(str, lst)))

# best practices
'''
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(' ')]
    return "%i %i" % (max(nn), min(nn))
'''

'''
What I learned/noticed from this solution:
* list comprehension is powerful – yet I still have a hard time
implementing it
* the use of f-string comes in handy for the best-practice solution,
while mine has to go throgh several steps (convert elements of a list
from string to integer and join them)
'''

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
print(high_and_low("10 2 -2 -10"))
print(high_and_low("1 -1"))
print(high_and_low("1 1"))
print(high_and_low("-1 -1"))
print(high_and_low("1 -1 0"))
print(high_and_low("1 1 0"))
print(high_and_low("-1 -1 0"))
print(high_and_low("42"))
