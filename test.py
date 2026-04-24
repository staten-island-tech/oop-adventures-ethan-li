# import time
# # 1. Record the start time at the very beginning
# start_time = time.perf_counter()

# # ... your code here ...
# time.sleep(2)  # Example delay

# # 2. Calculate and print elapsed time
# elapsed_time = time.perf_counter() - start_time
# print(f"Time since start: {elapsed_time:.2f} seconds")



# import random
# print(random.randint(1, 10))
import math
ans = 10/6
if ans - int(ans) >= 0.5:
    math.ceil(ans)
elif ans - int(ans) < 0.5:
    math.floor(ans)

