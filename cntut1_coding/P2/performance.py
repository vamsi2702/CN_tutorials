import matplotlib.pyplot as plt

clients = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
single_process = [30.100307019, 60.154269502, 90.191870225, 120.305613736, 150.361816081, 180.532423868, 210.60314716, 240.449743061, 270.540862131, 300.678368797]
multi_process = [3.080042614, 3.123898842, 3.202927958, 3.237070865, 3.2515205, 3.236693049, 3.308828197, 3.346927606, 3.348948647, 3.432797447]
multi_threaded = [3.083286023, 3.095704098, 3.112022116, 3.160507064, 3.206365764, 3.269937545, 3.312848983, 3.383327567, 3.517049328, 3.613411392]
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.plot(clients, single_process, label='Single-Process')
plt.plot(clients, multi_process, label='Multi-Process')
plt.plot(clients, multi_threaded, label='Multi-Threaded')
plt.xlabel('Number of Concurrent Clients')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()