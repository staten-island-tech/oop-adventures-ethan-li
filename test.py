import time
# 1. Record the start time at the very beginning
start_time = time.perf_counter()

# ... your code here ...
time.sleep(2)  # Example delay

# 2. Calculate and print elapsed time
elapsed_time = time.perf_counter() - start_time
print(f"Time since start: {elapsed_time:.2f} seconds")



# import random
# import math
# ans = float(input("WHat"))
# if ans - math.floor(ans) >= 0.5:
#     print(math.ceil(ans))
# elif ans - math.floor(ans) < 0.5:
#     print(math.floor(ans))
# print(round(random.uniform(0, 100/ans), 2))

