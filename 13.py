from ipaddress import *
net = ip_network(f'172.16.168.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 != 0:
        cnt += 1
print(cnt)
