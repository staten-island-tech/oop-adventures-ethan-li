import random
import time
#Golf incremental


types = [
    {'class': 'justin Lin', 
     'multi': 1, 
     'cooldown': 1, 
     'accuracy': 1, 
     'desc': "Average guy"},

    {'class': 'sharpshooter', 
     'multi': 1, 
     'cooldown': 1.2, 
     'accuracy': 1.1, 
     'desc': "Pro: Increased accuracy Con: Increased cooldown"},

    {'class': 'abuser', 
     'multi': 1, 
     'cooldown': 0.8, 
     'accuracy': 0.8, 
     'desc': "Pro: Decreased cooldown Con: Decreased accuracy"},

    {'class': 'midas', 
     'multi': 1.25, 
     'cooldown': 1.1, 
     'accuracy': 0.925, 
     'desc': "Pro: Increased mutli Con: Increased cooldown and decreased accuracy"}
]

print("Class list:")
for type in types:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(type['class'].capitalize())
    print(type['desc'])
    if type['class'] == "midas":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    time.sleep(0.5)

class_types = input("What class?").lower()

for type1 in types:
    if class_types in type1['class']:
        multi = type1['mutli']
        cooldown = type1['cooldown']
        accuracy = type1['accuracy']


class type:
    def __init__(self):
        self.class_type = class_types.capitalize()
        self.multi = multi
        self.cooldown = cooldown
        self.accuracy = accuracy

    
    