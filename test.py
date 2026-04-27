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
# import math
# ans = float(input("what"))
# if ans - math.floor(ans) >= 0.5:
#     print(math.ceil(ans))
# elif ans - math.floor(ans) < 0.5:
#     print(math.floor(ans))




# import random
# import math
# # ans = float(input("what"))
# # if ans - math.floor(ans) >= 0.5:
# #     print(math.ceil(ans))
# #     ans = math.ceil(ans)
# # elif ans - math.floor(ans) < 0.5:
# #     print(math.floor(ans))
# #     ans = math.floor(ans)
# # random_num = random.randint(1, 100/ans)
# # print(random_num)

# print(round(random.uniform(1, 10), 100000))






import random
import math
ans = float(input("WHat"))
if ans - math.floor(ans) >= 0.5:
    print(math.ceil(ans))
elif ans - math.floor(ans) < 0.5:
    print(math.floor(ans))
print(round(random.uniform(1, 100/ans), 2))