albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
# album name, artists name, release year, song list

# The title of the song "The Way I Choose" from the "Bad Company" album.
# The year that the album "Nightflight" was released.
# The track number of the song "Kentish Town Waltz" from the Imelda May album "More Mayhem".
# The tuple representing the song "Keeping a Rendezvous" from the Budgie album "Nightflight". 

# simple way.
print("-"*10,end='')
print("-"*30)
print("python in the simple way")
print(albums[1][3][5][1])  # The Way I Choose
print(albums[2][2])        # 1981
print(albums[3][3][3][0])  # 4
print(albums[2][3][1])     # (2, 'Keeping a Rendezvous')
print("#"*30)

print("-"*10,end='')
print("python in the hardway")
print("-"*30)
# hard way
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
