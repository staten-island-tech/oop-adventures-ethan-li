import random
import time
import math
#Golf incremental


types = [
    {'class': 'justin', 
     'multi': 1, 
     'cooldown': 1, 
     'accuracy': 1, 
     'desc': "Average guy",
     'money': 0
     },

    {'class': 'sharpshooter', 
     'multi': 1, 
     'cooldown': 1, 
     'accuracy': 1.1, 
     'desc': "Pro: Increased accuracy Con: Dept",
     'money': -50
     },

    {'class': 'abuser', 
     'multi': 1, 
     'cooldown': 0.8, 
     'accuracy': 0.8, 
     'desc': "Pro: Decreased cooldown Con: Decreased accuracy",
     'money': 0
     },

    {'class': 'midas', 
     'multi': 1.25, 
     'cooldown': 1.0, 
     'accuracy': 0.925, 
     'desc': "Pro: Starter money Con: Decreased accuracy",
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

class_types = input("What class? ").lower()
goal = int(input("How much money you want to earn? "))

for type1 in types:
    if class_types in type1['class']:
        multi = type1['multi']
        cooldown = type1['cooldown']
        accuracy = type1['accuracy']
        money = type1['money']

base_money_earned = 1
money_placeholder = 0
upgrade_value_m_percent = 0.01
upgrade_value_c_percent = 0.01
upgrade_value_a_percent = 0.01

class type:
    def __init__(self):
        self.class_type = class_types.capitalize()
        self.multi = multi
        self.cooldown = cooldown
        self.accuracy = accuracy
        self.money = money
    

    def upgrade_m(self):
        upgrade_value_m = self.mutli*upgrade_value_m_percent
        upgrade_value_m_percent += 0.01
        return upgrade_value_m

    def update_m(self, m_value):
        self.multi += m_value
    

    def upgrade_c(self):
        upgrade_value_c = self.mutli*upgrade_value_c_percent
        upgrade_value_c_percent += 0.01
        return upgrade_value_c

    def update_c(self, c_value):
        self.cooldown -= c_value
    

    def upgrade_a(self):
        upgrade_value_a = self.mutli*upgrade_value_a_percent
        upgrade_value_a_percent += 0.01
        return upgrade_value_a

    def update_a(self, a_value):
        self.accuracy += a_value
    

    def update_mon(self, mon_value):
        self.money += mon_value
        
    
    def hit(self):
        ans = float(self.accuracy)
        if ans - math.floor(ans) >= 0.5:
            print(math.ceil(ans))
        elif ans - math.floor(ans) < 0.5:
            print(math.floor(ans))
        ans = round(random.uniform(1, 100/ans), 2)
        if self.accuracy >= ans:
            self.money += base_money_earned * self.multi * 2
            money_placeholder += base_money_earned * self.multi * 2
        else:
            self.money += base_money_earned * self.multi
            money_placeholder += base_money_earned * self.multi


player = type()
while money_placeholder <= goal:
    print(f"Character: {class_types.capitalize()}")
    print(f"Money: {player.money}")
    print(f"Money Multi: {player.multi}")
    print(f"Cooldown : {player.cooldown-1:.2f}%")
    break




