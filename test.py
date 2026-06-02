# import time
# # 1. Record the start time at the very beginning
# start_time = time.perf_counter()

# # ... your code here ...
# time.sleep(2)  # Example delay

# # 2. Calculate and print elapsed time
# elapsed_time = time.perf_counter() - start_time
# print(f"Time since start: {elapsed_time:.2f} seconds")



# import random
# import math
# ans = float(input("WHat"))
# if ans - math.floor(ans) >= 0.5:
#     print(math.ceil(ans))
# elif ans - math.floor(ans) < 0.5:
#     print(math.floor(ans))
# print(round(random.uniform(0, 100/ans), 2))


# def add():
#     wasd = 1 + 1
#     return wasd
# print(add())



# goal = int(input("How much money you want to earn? "))
# goals = int(input("How much money you want to earn?"))
# print(goal)
# print(goals)



# w = 1
# print(f"sdfasdf {w+1}")



# user_input = input("Enter something: ")

# if user_input.isdigit():
#     user_input = int(user_input)
#     print("Converted to integer.")
# else:
#     print("Kept as string.")




# x = input("y")
# def int_or_string(z):
#     if z.isdigit():
#         if int(z) >= 1:
#             print("greater than 1")
#         else:
#             print("less than one")
#     else:
#         print(z)
# int_or_string(x)



# x = 0
# def add():
#     if x < 10:
#         print(x)
#         return True
        
#     elif x >= 10:
#         print(x)
#         return False
        
    
# while add():
#     x += 1
#     add()



# import random
# round = round(random.uniform(1, 100/1.25), 2)
# print(round)



# import time

# class wasd:
#     def __init__(self, cooldown_seconds=2.0):
#         self.cooldown = cooldown_seconds
#         self.last_hit_time = 0  

#     def try_hit(self):
#         current_time = time.time()
#         if current_time - self.last_hit_time >= self.cooldown:
#             print("Hit successful!")
#             self.last_hit_time = current_time
#             return False
#         else:
#             print(f"Still on cooldown. Wait {self.cooldown - (current_time - self.last_hit_time):.2f}s")
#             return True

# combat = wasd()

# while combat.try_hit() is True:

    
#     combat.try_hit()
#     time.sleep(0.25) 
# while combat.try_hit() is True:

    
#     combat.try_hit() 
#     time.sleep(0.25)
# import random
# import math
# # difficult = random.randint(1, 3)
# # print(difficult)
# # print(math.floor(4.8))

# run = 19000
# second = run
# minute = run/60
# hour = run/3600

# if run < 60:
#     print(f'Run time: {second:.0f} seconds')
# elif run >= 60 and run < 3600:
#     minute = run/60
#     second = (run/60 - math.floor(minute))*60
#     print(f"Run time: {minute:.0f} minutes and {second:.0f} seconds")
# elif run >= 3600:
#     minute -= math.floor(hour)*60
#     second -= (math.floor(minute)*60) + (math.floor(hour)*3600)
#     print(f"Run time: {math.floor(hour)} hours; {math.floor(minute)} minutes a;  {second:.0f} seconds")




# for words in "easy":
#     for word in "very easy":
#         if word in words:
#             print("yes")






# difficulty = input("wasd").lower()


# for x in difficulty:
#     if x in "easy":
#         print("Easy Mode: 0.5x Goal and 2x money")
#         base_money_earned = 10*2
#         goal = 1000/2
#         print("Goal: $" + str(goal))
#         break
#     elif x in "normal":
#         print("Normal Mode: No modification")
#         base_money_earned = 10
#         goal = 1000
#         print("Goal: $" + str(goal))
#     elif x in "hard":
#         print("Hard Mode: 2x cost")
#         base_money_earned = 10 
#         goal = 1000
#         m = 2
#         c = 2
#         a = 2
#         print("Goal: $" + str(goal))
#         break
#     elif x in "extreme":
#         print("Extreme Mode: 2x goal and 2x cost")
#         base_money_earned = 10
#         goal = 1000*2
#         m = 2
#         c = 2
#         a = 2
#         print("Goal: $" + str(goal))
#         break
#     elif x in "qwerty":
#         print("Dev mode")
#         base_money_earned = 10
#         goal = 10000
#         mm = 0
#         m = 0
#         c = 0
#         a = 0
#         cooldown = 2
#         break




import os
import sys

def restart_program():
    print("Restarting")
    os.execv(sys.executable, ['python'] + sys.argv)

print("hi")
answer = input("Type 'restart' to play again: ")
if answer == "restart":
    restart_program()