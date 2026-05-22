import random
import time
import math
import requests
start = time.time()

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
     'desc': "Slightly average guy",
     'money': 0
     },

    {'class': 'sharpshooter', 
     'multi': 1, 
     'cooldown': 1, 
     'accuracy': 1.25, 
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
     'accuracy': 0.8, 
     'desc': "Pro: Starter money Con: Decreased accuracy",
     'money': 10000000
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
difficulty = input("What difficulty? ").lower()  # Add Diffuclty mode #   Easy - 2x money   Normal - Normal     Hard - 1.5x cost  Extreeme - 2x cost + 1/2x money 

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
time.sleep(0.25)

for type1 in types:
    if class_types in type1['class']:
        multi = type1['multi']
        cooldown = type1['cooldown']
        accuracy = type1['accuracy']
        money = type1['money']

m = 1
c = 1
a = 1
mm = 1


if difficulty == "easy":
    print("Easy Mode: 0.5x Goal and 2x money")
    base_money_earned = 10*2
    goal = 1000/2
    print("Goal: $" + str(goal))
elif difficulty == "normal":
    print("Normal Mode: No modification")
    base_money_earned = 10
    goal = 1000
    print("Goal: $" + str(goal))
elif difficulty == "hard":
    print("Hard Mode: 2x cost")
    base_money_earned = 10 
    goal = 1000
    m = 2
    c = 2
    a = 2
    print("Goal: $" + str(goal))
elif difficulty == "extreme":
    print("Extreme Mode: 2x goal and 2x cost")
    base_money_earned = 10
    goal = 1000*2
    m = 2
    c = 2
    a = 2
    print("Goal: $" + str(goal))
elif difficulty == "qwerty":
    print("Dev mode")
    base_money_earned = 10
    goal = 10000
    mm = 0
    m = 0
    c = 0
    a = 0
    cooldown = 50


class type:
    def __init__(self):
        self.class_type = class_types.capitalize()
        self.multi = multi
        self.cooldown = cooldown
        self.accuracy = accuracy
        self.money = money*mm
        self.upgrade_value_m_percent = 0.1
        self.upgrade_value_c_percent = 0.2
        self.upgrade_value_a_percent = 0.3
        self.upgrade_value_m_percent_cost = 0.25
        self.upgrade_value_c_percent_cost = 0.5
        self.upgrade_value_a_percent_cost = 0.75
        self.cost_m = 10*m
        self.cost_c = 20*c
        self.cost_a = 50*a
        self.cooldown_time = 10/self.cooldown
        self.last_hit_time = 0  

        self.total_upgrade = 0
        self.total_hit = 0
        self.total_m = 0
        self.total_c = 0
        self.total_a = 0
        self.total_spent_m = 0
        self.total_spent_c = 0
        self.total_spent_a = 0
        self.total_spent = 0
        self.miss = 0
        self.hole_in_one = 0
        self.successful_hit = 0

    def upgrade_m(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("You have $" + str(self.money))
        yes_or_no = input(f"Upgrading Multi for ${self.cost_m:.2f} from {self.multi:.2f} x ---> {(self.multi+self.multi*self.upgrade_value_m_percent):.2f} x? (Yes/No) ").lower()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        time.sleep(0.25)
        if yes_or_no == "yes":
            if self.money >= self.cost_m:
                self.total_upgrade += 1
                self.total_m += 1
                self.total_spent += self.cost_m
                self.total_spent_m += self.cost_m
                self.money -= self.cost_m
                self.cost_m += self.cost_m*self.upgrade_value_m_percent_cost
                self.upgrade_value_m_percent_cost += 0.25
                self.multi += self.multi*self.upgrade_value_m_percent
                self.upgrade_value_m_percent += 0.1 
                print("You have $" + str(self.money))
                print(f"Current Money Multi: {self.multi:.2f} x")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                hit_or_upgrade(ready)
            elif self.money < self.cost_m:
                print("NOT ENOUGH MONEY!")          
        elif yes_or_no == "no": 
            print("Carry on")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


    def upgrade_c(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("You have $" + str(self.money))
        yes_or_no = input(f"Upgrading cooldown for ${self.cost_c:.2f} from {self.cooldown:.2f} x ---> {(self.cooldown+self.cooldown*self.upgrade_value_c_percent):.2f} x? (Yes/No) ").lower()
        print(f"Current Cooldown Time: {self.cooldown_time:.2f} seconds")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        time.sleep(0.25)
        if yes_or_no == "yes":
            if self.money >= self.cost_c:
                self.total_upgrade += 1
                self.total_c += 1
                self.total_spent += self.cost_c
                self.total_spent_c += self.cost_c
                self.money -= self.cost_c
                self.cost_c += self.cost_c*self.upgrade_value_c_percent_cost
                self.upgrade_value_c_percent_cost += 0.5
                self.cooldown += self.cooldown*self.upgrade_value_c_percent
                self.upgrade_value_c_percent += 0.2 
                print("You have $" + str(self.money))
                print("Current Cooldown Multi: " + str(self.cooldown) + "x")
                self.cooldown_time = 10/self.cooldown
                print(f"Cooldown: {self.cooldown_time:.2f} seconds")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                hit_or_upgrade(ready)
            elif self.money < self.cost_c:
                print("NOT ENOUGH MONEY!")
        elif yes_or_no == "no":
            print("Carry on")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


    def upgrade_a(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("You have $" + str(self.money))
        yes_or_no = input(f"Upgrading accuracy for ${self.cost_a:.2f} from {self.accuracy:.2f} x ---> {(self.accuracy+self.accuracy*self.upgrade_value_a_percent):.2f} x? (Yes/No) ").lower()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        time.sleep(0.25)
        if yes_or_no == "yes":
            if self.money >= self.cost_a:
                self.total_upgrade += 1
                self.total_a += 1
                self.total_spent += self.cost_a
                self.total_spent_a += self.cost_a
                self.money -= self.cost_a
                self.cost_a += self.cost_a*self.upgrade_value_a_percent_cost
                self.upgrade_value_a_percent_cost += 0.75
                self.accuracy += self.accuracy*self.upgrade_value_a_percent
                self.upgrade_value_a_percent += 0.3
                print("You have $" + str(self.money))
                print(f"Current Accuracy Multi {self.accuracy:.2f}x")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                hit_or_upgrade(ready)
            elif self.money < self.cost_a:
                print("NOT ENOUGH MONEY")
        elif yes_or_no == "no":
            print("Carry on")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
             
    
    def hit(self):
        current_time = time.time()
        if current_time - self.last_hit_time >= self.cooldown_time:
            self.last_hit_time = current_time
            hit_or_miss = random.randint(1, 100)
            self.total_hit += 1
            if hit_or_miss > 50:
                divide = self.accuracy
                est = round(random.uniform(1, 50/divide), 2)
                if self.accuracy >= est:
                    print("HOLE IN ONE!")
                    self.money += base_money_earned * self.multi * 2
                    print("$ " + str(self.money))
                    self.hole_in_one += 1
                else:
                    print("HIT!")
                    self.money += base_money_earned * self.multi
                    print("$ " + str(self.money))
                    self.successful_hit += 1
            elif hit_or_miss <= 50:
                print("MISS!")
                self.miss += 1
        else:
            print(f"Still on cooldown. Wait {self.cooldown_time - (current_time - self.last_hit_time):.2f}s")
        

    def show_stats(self):
        print(f"Character: {class_types.capitalize()}")
        print(f"Money: ${player.money:.2f}")
        print(f"Money Multi: {player.multi:.2f}x")
        if player.cooldown-1 > 0:
            print(f"Cooldown: {player.cooldown-1:.1f}% faster")
        elif player.cooldown-1 < 0:
            print(f"Cooldown: {player.cooldown-1:.1f}% slower")
        elif player.cooldown-1 == 0:
            print(f"Cooldown: 0% - Normal")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")  

    
player = type()


def hit_or_upgrade(x):
    if x == "hit":
        player.hit()
    
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
    ready = str(input("Hit or Upgrade? ").lower())
    hit_or_upgrade(ready)
    

end = time.time()
run = end - start
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -") 
print("Final Test: (Correct = win   Wrong = lose)")


def getRiddle(difficulty):
    response = requests.get(f"https://api.apileague.com/retrieve-random-riddle?api-key=1f532a394a454ca5a7b997b4a8031c40&difficulty={difficulty.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    

    data = response.json()
    answer = data['answer']
    riddle = data['answer']
    return answer, riddle


difficulty_gen = random.randint(1, 3)
if difficulty_gen == 1:
    difficult = "easy"
elif difficulty_gen == 2:
    difficult = "medium"
elif difficulty_gen == 3:
    difficult = "hard"


x, y = getRiddle(difficult)


for words in x:
    question = input(y)
    for word in question:
        if question in words:
            print("Correct")
        else:
            print("Wrong")


print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")  
print('YOU BEAT THE GAME!')
time.sleep(1.5)
print(f'Run time: {run:.0f} seconds')
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")  
print("Game Stats:")
print(f"Total Upgrade Amount: {player.total_upgrade} upgrades for ${player.total_spent:.2f}")
print(f"Total Money Multi Upgrade Amount: {player.total_m} upgrades for ${player.total_spent_m}")
print(f"Total Cooldown Upgrade Amount: {player.total_c} upgrades for ${player.total_spent_c}")
print(f"Total Accuracy Upgrade Amount: {player.total_a} upgrades for ${player.total_spent_a}")
print(f"Total Times Hit: {player.total_hit} hits") 
print(f"Successful Hit: {player.successful_hit} hits")
print(f"Hole in One: {player.hole_in_one} hole in ones")
print(f"Missed Hit: {player.miss}")
time.sleep(5)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")  
player.show_stats()