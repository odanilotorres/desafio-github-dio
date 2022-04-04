import os
import time

with open('hosts') as file:
    dump = file.read()
    dump = dump.splitlines()

    print('-' * 60)
    print('<>' * 30)
    print('-' * 60)
    for ip in dump:
        print(('-' * 15) + ' Escaneando IP: {} '.format(ip) + ('-' * 15))
        os.system('ping -c 4 {}'.format(ip))
        print('-' * 60)
        print('<>' * 30)
        print('-' * 60)
        time.sleep(3)