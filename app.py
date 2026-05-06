import random
import time
import math
#Golf incremental

print("Welcome to Golf Incremental!")
time.sleep(1)
print("Reach your goal ro ascend")  
time.sleep(1)
print("Ascend to get accession points")
time.sleep(1)
print("Use accession points on skill tree")
time.sleep(1)
print("Hole in ones give 2x money")
time.sleep(1)
print("Missing does not give extra multiplier")
time.sleep(5)


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


class type:
    def __init__(self):
        self.class_type = class_types.capitalize()
        self.multi = multi
        self.cooldown = cooldown
        self.accuracy = accuracy
        self.money = money
        self.upgrade_value_m_percent = 0.05
        self.upgrade_value_c_percent = 0.03
        self.upgrade_value_a_percent = 0.02
        self.upgrade_value_m_percent_cost = 0.01
        self.upgrade_value_c_percent_cost = 0.02
        self.upgrade_value_a_percent_cost = 0.03
        self.cost_m = 1
        self.cost_c = 5
        self.cost_a = 10

        
    

    def upgrade_m(self):
        if self.money >= self.cost_m:
            self.money -= cost_m
            cost_m = cost_m*self.upgrade_value_m_percent_cost
            self.upgrade_value_m_percent_cost += 0.01
            self.multi += self.multi*self.upgrade_value_m_percent
            self.upgrade_value_m_percent += 0.05
        elif self.money < cost_m:
            print("NOT ENOUGH MONEY!")
            trail += 1
            


    def upgrade_c(self):
        if self.money >= self.cost_c:
            self.money -= cost_c
            cost_c = cost_c*self.upgrade_value_c_percent_cost
            self.upgrade_value_c_percent_cost += 0.02
            self.cooldown += self.cooldown*self.upgrade_value_c_percent
            self.upgrade_value_c_percent += 0.03 
        elif self.money < cost_c:
            print("NOT ENOUGH MONEY")
            trail += 1
        


    def upgrade_a(self):
        if self.money >= self.cost_a:
            self.money -= cost_a
            cost_a = cost_a*self.upgrade_value_a_percent_cost
            self.upgrade_value_a_percent_cost += 0.03
            self.accuracy += self.accuracy*self.upgrade_value_a_percent
            self.upgrade_value_a_percent += 0.02
        elif self.money < cost_a:
            print("NOT ENOUGH MONEY")
            trail += 1
            
        
    
    def hit(self):
        ans = float(self.accuracy)
        if ans - math.floor(ans) >= 0.5:
            print(math.ceil(ans))
        elif ans - math.floor(ans) < 0.5:
            print(math.floor(ans))
        round = round(random.uniform(1, 100/ans), 2)
        if self.accuracy >= round:
            print("HOLE IN ONE!")
            self.money += base_money_earned * self.multi * 2
        else:
            print("MISS!")
            self.money += base_money_earned * self.multi
    

    def show_stats(self):
        print(f"Character: {class_types.capitalize()}")
        print(f"Money: ${player.money}")
        print(f"Money Multi: {player.multi}x")
        if player.cooldown-1 > 0:
            print(f"Cooldown: {player.cooldown-1:.2f}% faster")
        elif player.cooldown-1 < 0:
            print(f"Cooldown: {player.cooldown-1:.2f}% slower")
        elif player.cooldown-1 == 0:
            print(f"Cooldown: 0% - Normal")

            
player = type()


def hit_or_upgrade(x):
    if x == "hit":
        player.hit()
    elif x == "upgrade":
        upgrade_type = input("What do you want to upgrade? (Multi/Cooldown/Accuracy)").lower()
        if upgrade_type == "multi":
            player.upgrade_m()
        elif upgrade_type == "cooldown":
            player.upgrade_c()
        elif upgrade_type == "accuracy":
            player.upgrade_a()


while player.money <= goal:
    player.show_stats()
    time.sleep(2)
    ready = str(input("Hit or Upgrade?").lower())
    hit_or_upgrade(ready)

    

# fix cost_m