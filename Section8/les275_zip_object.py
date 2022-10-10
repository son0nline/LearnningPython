albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ["album",'artist','year']

for album in albums:
    zip_object = zip(keys,album)
    print(zip_object, type(zip_object))
    #print('dict:', dict(zip_object))
    for data in zip_object:
        title, value = data
        print('\t', type(data), data)
        print('\t',title, value)
        