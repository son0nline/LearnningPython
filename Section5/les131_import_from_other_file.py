#import variable albums from file les131_nested_data.py
from les131_nested_data import albums

lsAnswers = list(range(4))
for album in albums:
    songs = album[3]

    for song in songs:
        trackId, song_name = song
        if song_name == "The Way I Choose":
            #print(song_name)
            lsAnswers[0] = song_name
        elif song_name == "Kentish Town Waltz":
            #print(trackId)
            lsAnswers[2] = trackId
        elif song_name == "Keeping a Rendezvous" and album[0] == "Nightflight":
            #print(song)
            lsAnswers[3] = song

    if "Nightflight" == album[0]:
        #print(album[2])
        lsAnswers[1] = album[2]

for answer in lsAnswers:
    print(answer)