# SQUARE EVERY DIGIT OF A NUMBER
# For example, if passed in number 9119,
# 81181 will come out, for 9**2 = 81 and 1**1 = 1

# my solution:
def square_digits(num):
    result = 0
    unit = 1

    while num >= 1:
        result += (num % 10)**2 * unit
        num = int(num / 10)

        while result >= unit:
            unit *= 10
    return(result)

# best practice:
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)


# why I didn't do something alike:
# * I wanted to apply Math
# * I tried but mine was lengthy and hard to understand

# what's great about this practice:
# * it's short but get to the point
# * it's not complicated and show that the user
# is skilfull in manipulating types of variables
# * it's something a beginner like me can understand


# clever:
# def square_digits(num):
#     return int(''.join(str(int(c)**2) for c in str(num)))


# I have never known how to use join()
# I think this one is like the above, converting the variable
# between string and integer, not much cleverer.

print(square_digits(9119))
