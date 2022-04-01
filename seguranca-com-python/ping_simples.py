import os #importanto o modulo os
print('#' * 60)
ip_ou_host = input('Digite o IP ou HOST a ser verificado: ')
print('-' * 60)
print(os.system('ping -c 6 {}'.format(ip_ou_host)))
print('-' * 60)