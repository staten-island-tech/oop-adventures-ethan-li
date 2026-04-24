import random
import time
#Golf incremental


types = [
    {'class': 'justin Lin', 
     'multi': 1, 
     'cooldown': 1, 
     'accuracy': 1, 
     'desc': "Average guy"
     'money': 0
     },

    {'class': 'sharpshooter', 
     'multi': 1, 
     'cooldown': 1, 
     'accuracy': 1.1, 
     'desc': "Pro: Increased accuracy Con: Dept"
     'money': -50
     },

    {'class': 'abuser', 
     'multi': 1, 
     'cooldown': 0.8, 
     'accuracy': 0.8, 
     'desc': "Pro: Decreased cooldown Con: Decreased accuracy"
     'money': 0
     },

    {'class': 'midas', 
     'multi': 1.25, 
     'cooldown': 1.1, 
     'accuracy': 0.925, 
     'desc': "Pro: Increased mutli Con: Increased cooldown and decreased accuracy"
     'money': 100
     }
]

print("Class list:")
for type in types:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(type['class'].capitalize())
    print(type['desc'])
    if type['class'] == "midas":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    time.sleep(0.25)

class_types = input("What class?").lower()

for type1 in types:
    if class_types in type1['class']:
        multi = type1['multi']
        cooldown = type1['cooldown']
        accuracy = type1['accuracy']
        money = type1['money']


class type:
    def __init__(self):
        self.class_type = class_types.capitalize()
        self.multi = multi
        self.cooldown = cooldown
        self.accuracy = accuracy
        self.money = money
    
    def update_m(self, m_value):
        self.multi += m_value
    
    def update_c(self, c_value):
        self.cooldown += c_value
    
    def update_a(self, a_value):
        self.accuracy += a_value
    
    def update_m(self, m_value):
        self.money += m_value
    
    def hit(self):
        random.randint(1, int(100/self.accuracy)



