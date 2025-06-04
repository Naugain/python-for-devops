# Integer: Whole numbers
servers = 5
print("Number of servers:", servers)
print("Type of servers:", type(servers))

# Float: Decimal numbers
cpu_usage = 75.5
print("CPU usage (%):", cpu_usage)
print("Type of cpu_usage:", type(cpu_usage))

# Simple math
total_servers = servers + 3
avg_load = cpu_usage / servers
print("Total servers after adding 3:", total_servers)
print("Average CPU load per server:", avg_load)

# Strings: Text data
server_name = "web-server-01"
log_message = 'System rebooted successfully'
print("Server name:", server_name)
print("Log message:", log_message)
print("Type of server_name:", type(server_name))

# String operations
upper_name = server_name.upper()
concat_message = server_name + ": " + log_message
print("Uppercase server name:", upper_name)
print("Concatenated message:", concat_message)

# Booleans: True or False
is_server_online = True
is_backup_complete = False
print("Is server online?", is_server_online)
print("Is backup complete?", is_backup_complete)
print("Type of is_server_online:", type(is_server_online))

# Boolean operations
can_deploy = is_server_online and not is_backup_complete
print("Can deploy now?", can_deploy)

# Lists: Ordered, mutable collection
server_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
print("Server IPs:", server_ips)
print("Type of server_ips:", type(server_ips))

# List operations
server_ips.append("192.168.1.4")  # Add new IP
first_ip = server_ips[0]  # Access first IP
print("Updated server IPs:", server_ips)
print("First IP:", first_ip)
print(len(first_ip))

# Dictionaries: Key-value pairs
server_config = {
    "name": "web-server-01",
    "port": 8080,
    "is_active": True
}
print("Server config:", server_config)
print("Type of server_config:", type(server_config))

# Dictionary operations
port = server_config["port"]
server_config["memory"] = "16GB"  # Add new key-value pair
print("Server port:", port)
print("Updated config:", server_config)

'''
Output of the above code
kunal@Kunal:~/lessons/python-for-devops/Practice$ python3 datatypes.py
Number of servers: 5
Type of servers: <class 'int'>
CPU usage (%): 75.5
Type of cpu_usage: <class 'float'>
Total servers after adding 3: 8
Average CPU load per server: 15.1
Server name: web-server-01
Log message: System rebooted successfully
Type of server_name: <class 'str'>
Uppercase server name: WEB-SERVER-01
Concatenated message: web-server-01: System rebooted successfully
Is server online? True
Is backup complete? False
Type of is_server_online: <class 'bool'>
Can deploy now? True
Server IPs: ['192.168.1.1', '192.168.1.2', '192.168.1.3']
Type of server_ips: <class 'list'>
Updated server IPs: ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
First IP: 192.168.1.1
11
Server config: {'name': 'web-server-01', 'port': 8080, 'is_active': True}
Type of server_config: <class 'dict'>
Server port: 8080
Updated config: {'name': 'web-server-01', 'port': 8080, 'is_active': True, 'memory': '16GB'}
'''