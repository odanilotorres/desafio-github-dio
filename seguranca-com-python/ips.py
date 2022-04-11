import ipaddress

# ip = '192.168.0.1'
# endereco = ipaddress.ip_address(ip)
#
# print(endereco)
# print(endereco + 100)
# print(endereco + 257)


ip = '192.168.0.0/24'
# rede = ipaddress.ip_network(ip)
rede = ipaddress.ip_network(ip, strict=False)
# print(rede)

for ip in rede:
    print(ip)