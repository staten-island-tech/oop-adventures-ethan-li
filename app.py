import random
import time
import math
#Golf incremental

print("Welcome to Golf Incremental!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
time.sleep(1)
print("Reach your goal to ascend")  
time.sleep(1)
print("Ascend to get accession points")
time.sleep(1)
print("Use accession points on skill tree")
time.sleep(1)
print("Hole in ones give 2x money and landing a hit gives no extra multiplier")
time.sleep(1)
print("Missing does not give money")
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

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Class list:")
for type in types:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(type['class'].capitalize())
    print(type['desc'])
    if type['class'] == "midas":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    time.sleep(0.25)

class_types = input("What class? ").lower()
goal = int(input("How much money you want to earn? "))  # Add Diffuclty mode #   Easy - like this   Mid - 1.5x cost     Hard - 2x cost  
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
time.sleep(0.25)

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
        self.upgrade_value_m_percent = 0.1
        self.upgrade_value_c_percent = 0.2
        self.upgrade_value_a_percent = 0.3
        self.upgrade_value_m_percent_cost = 0.25
        self.upgrade_value_c_percent_cost = 0.5
        self.upgrade_value_a_percent_cost = 0.75
        self.cost_m = 10
        self.cost_c = 20
        self.cost_a = 50

        
    

    def upgrade_m(self):
        print("You have $" + str(self.money))
        yes_or_no = input("Upgrading Multi for $" + str(self.cost_m) + " from " + str(self.multi) + "x ---> " + str(self.multi+self.multi*self.upgrade_value_m_percent) + "x? (Yes/No) ").lower()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        time.sleep(0.25)
        if yes_or_no == "yes":
            if self.money >= self.cost_m:
                self.money -= self.cost_m
                self.cost_m = self.cost_m*self.upgrade_value_m_percent_cost
                self.upgrade_value_m_percent_cost += 0.25
                self.multi += self.multi*self.upgrade_value_m_percent
                self.upgrade_value_m_percent += 0.1 
                print("You have $" + str(self.money))
                print("Current Money Multi: " + str(self.multi))
                hit_or_upgrade(ready)
            elif self.money < self.cost_m:
                print("NOT ENOUGH MONEY!")          
        elif yes_or_no == "no": 
            print("Carry on")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    def upgrade_c(self):
        print("You have $" + str(self.money))
        yes_or_no = input("Upgrading Multi for $" + str(self.cost_c) + " from " + str(self.cooldown) + " ---> " + str(self.cooldown+self.cooldown*self.upgrade_value_c_percent) + "? (Yes/No) ").lower()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        time.sleep(0.25)
        if yes_or_no == "yes":
            if self.money >= self.cost_c:
                self.money -= self.cost_c
                self.cost_c = self.cost_c*self.upgrade_value_c_percent_cost
                self.upgrade_value_c_percent_cost += 0.5
                self.cooldown += self.cooldown*self.upgrade_value_c_percent
                self.upgrade_value_c_percent += 0.2 
                print("You have $" + str(self.money))
                print("Current Cooldown Multi: " + str(self.cooldown))
                hit_or_upgrade(ready)
            elif self.money < self.cost_c:
                print("NOT ENOUGH MONEY!")
        elif yes_or_no == "no":
            print("Carry on")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


    def upgrade_a(self):
        print("You have $" + str(self.money))
        yes_or_no = input("Upgrading Multi for $" + str(self.cost_a) + " from " + str(self.accuracy) + "x ---> " + str(self.accuracy+self.accuracy*self.upgrade_value_c_percent) + "x? (Yes/No) ").lower()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        time.sleep(0.25)
        if yes_or_no == "yes":
            if self.money >= self.cost_a:
                self.money -= self.cost_a
                self.cost_a = self.cost_a*self.upgrade_value_a_percent_cost
                self.upgrade_value_a_percent_cost += 0.75
                self.accuracy += self.accuracy*self.upgrade_value_a_percent
                self.upgrade_value_a_percent += 0.3
                print("You have $" + str(self.money))
                print("Current Accuracy Multi " + str(self.accuracy))
                hit_or_upgrade(ready)
            elif self.money < self.cost_a:
                print("NOT ENOUGH MONEY")
        elif yes_or_no == "no":
            print("Carry on")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

             
    
    def hit(self):
        hit_or_miss = random.randint(1, 100)
        if hit_or_miss > 50:
            divide = self.accuracy
            est = round(random.uniform(1, 100/divide), 2)
            if self.accuracy >= est:
                print("HOLE IN ONE!")
                self.money += base_money_earned * self.multi * 2
                print("$ " + str(self.money))
            else:
                print("HIT!")
                self.money += base_money_earned * self.multi
                print("$ " + str(self.money))
        else:
            print("MISS!")
        

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
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")  

    
player = type()


def hit_or_upgrade(x):
    if x == "hit":
        player.hit()
        # if time.perf_counter() - start_time > hit_cooldown:
        #     player.hit()
        # else:
        #     print("On Cooldown!")
    elif x == "upgrade":
        upgrade_type = input("What do you want to upgrade? (Multi/Cooldown/Accuracy/No upgrade) ").lower()
        if upgrade_type == "multi":
            player.upgrade_m()
        elif upgrade_type == "cooldown":
            player.upgrade_c()
        elif upgrade_type == "accuracy":
            player.upgrade_a()

player.show_stats()

while player.money <= goal:
    start_time = time.perf_counter()
    hit_cooldown = 10 * player.cooldown
    time.sleep(1)
    ready = str(input("Hit or Upgrade? ").lower())
    hit_or_upgrade(ready)
    

    

