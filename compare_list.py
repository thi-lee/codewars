# set 1 True
array1 = [4, 4]
array2 = [1, 31]
# set 2 True
# array1 = [121, 144, 19, 161, 19, 144, 19, 11]
# array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# # set 3 False
# array1 = [121, 144, 19, 161, 19, 144, 19, 11]
# array2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# # set 4 False
# array1 = [121, 144, 19, 161, 19, 144, 19, 11]
# array2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
# # set 5 False
# array1 = []
# array2 = None
# # set 6 False
# array1 = [10000001, 100000000]
# array2 = [10000000 * 10000000, 100000000 * 100000000]

# my solution:
if array1 is None or array2 is None:
    print(False)

aprime = sorted([i * i for i in array1])
print(aprime == sorted(array2))


# return directly instead of using if else
# such as if two lists not equal then return False

# best practice:

# try:
#     print(sorted([i ** 2 for i in array1]) == sorted(array2))
# except:
#     print(False)

# I think try/except is cool but I have never applied it
