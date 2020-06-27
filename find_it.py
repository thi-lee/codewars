# Given an array, find the integer that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

# My solution
def find_it(seq):
    counts = dict()

    for num in seq:
        counts[num] = counts.get(num, 0) + 1

    for key, value in counts.items():
        if value % 2 != 0:
            return key

# best practice
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

# This is the first time I know about .count()
# I'll try to use this for other challenges that
# involve counting.

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
