import json

ip_counter = {}
commands = []

with open('var/log/cowrie/cowrie.json', 'r') as f:
    for line in f:
        data = json.loads(line)
        if 'src_ip' in data:
            ip = data['src_ip']
            ip_counter[ip] = ip_counter.get(ip, 0) + 1
        if data.get('eventid') == 'cowrie.command.input':
            commands.append(data['input'])

print("Top Attacker IPs:")
for ip, count in sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{ip}: {count} attempts")

print("\nSample Commands Used:")
for cmd in set(commands[:10]):
    print(cmd)
