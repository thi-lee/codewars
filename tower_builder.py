# my solution:
def tower_builder(n_floors):
    lst = []
    j = 0
    for i in range(n_floors, 0, -1):
        star = i * 2 - 1
        lst.insert(0, ' ' * j + '*' * star + ' ' * j)
        j += 1

    return(lst)

# clever and best practice:
'''
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
'''

'''
I have never known about .center(), great thing I came across this :)
I should work more on putting list comprehension into practice
'''

print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
