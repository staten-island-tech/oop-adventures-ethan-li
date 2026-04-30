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

x = input("y")
def int_or_string(z):
    if z.isdigit():
        if int(z) >= 1:
            print("greater than 1")
        else:
            print("less than one")
    else:
        print(z)
int_or_string(x)