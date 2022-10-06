from hashlib import md5


available_parts = ["computer",
                    "monitor",
                    "keyboard",
                    "mouse",
                    "hdmi cable",
                    "dvd drive",
                   ]

mDict = dict.fromkeys(available_parts, 'default value')
print(mDict)
print(mDict.keys())