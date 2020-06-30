# Given a non-negative number,
# return the time in human-readable format (HH:MM:SS)

# my solution
def make_readable(n):
    (h, m) = (3600, 60)
    hour = int(n / h)
    n = n - hour * h
    minute = int(n / m)
    n = n - minute * m
    second = int(n)

    return("%02d:%02d:%02d" % (hour, minute, second))

'''
def make_readable(s):
    return('{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60))
'''

# I should note down floor division
# It's also interesting how mod of 60 can give you minute and second :)
# I was wondering about that when I did mine

print(make_readable(0))
print(make_readable(59))
print(make_readable(60))
print(make_readable(3599))
print(make_readable(3600))
print(make_readable(86399))
print(make_readable(86400))
print(make_readable(359999))
