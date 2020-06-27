# my solution:
def song_decoder(song):
    song = song.replace('WUB', ' ').split()
    return ' '.join(song)

print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))

'''
my solution is really close to the best-practice attempt
i'm proud :)
I could have replace song in return statement with the
second line, but I chose not to because I want it to
be readable.
'''
