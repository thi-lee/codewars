def generate_hashtag(s):
    # Check if string length is more than 140 characters
    if len(s) > 140 or len(s) < 1:
        return False
    # Create a list separate all words of string
    str1 = s.split()
    # Capitalize the first letter of each word and add to a different list
    str2 = [word.capitalize() for word in str1]
    # Join them together with hashtag at the beginning
    return '#' + ''.join(str2)

# most of the return statements go like this:
# return False if (len(s) == 0 or len(output) > 140) else output
# and that's something new I gotta learn how to do
# although I don't know if it's necessary :) 

print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag'))
print(generate_hashtag('Codewars'))
print(generate_hashtag('CodeWars is nice'))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
