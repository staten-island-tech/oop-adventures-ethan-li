import time
# 1. Record the start time at the very beginning
start_time = time.perf_counter()

# ... your code here ...
time.sleep(2)  # Example delay

# 2. Calculate and print elapsed time
elapsed_time = time.perf_counter() - start_time
print(f"Time since start: {elapsed_time:.2f} seconds")

# 1. Record the start time at the very beginning
new = time.perf_counter()

# ... your code here ...
time.sleep(2.12345)  # Example delay

# 2. Calculate and print elapsed time
elapsed_time = time.perf_counter() - new
print(f"Time since start: {elapsed_time:.3f} seconds")