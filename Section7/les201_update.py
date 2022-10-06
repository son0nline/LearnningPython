from mlib import print_dict


mDict1 = {  "1": "computer",
            "2": "monitor",
            "3": "keyboard",
            "4": "mouse",
            "5": "hdmi cable",
            "6": "dvd drive",
        }

mDict2 = {  
            "6": "power supply", # 6 will be updated
            "7": "ssd",
            "8": "graphic card",
            "9": "moderm"
        }

mDict1.update(mDict2)

print_dict(mDict1)