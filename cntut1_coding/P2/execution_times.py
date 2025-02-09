import subprocess
import time

def execute_benchmark(client_count):
    cmd = f"bash start.sh client.py {client_count}"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    
    # Parse execution time from stdout
    for line in stdout.decode().split('\n'):
        if "Total Execution Time:" in line:
            return float(line.split(":")[1].strip().split()[0])
    return None

client_numbers = list(range(10, 101, 10))
times = []

for num in client_numbers:
    print(f"Executing benchmark with {num} clients...")
    exec_time = execute_benchmark(num)
    if exec_time:
        times.append(exec_time)
    else:
        print(f"Error executing benchmark for {num} clients")
    time.sleep(2)  # Pause between runs to allow server reset

print("\nResults:")
print("Clients | Execution Time (s)")
print("--------|--------------------")
for num, exec_time in zip(client_numbers, times):
    print(f"{num:7d} | {exec_time:.6f}")

# We can now use client_numbers and times lists for further analysis or plotting
print(times)
print(client_numbers)