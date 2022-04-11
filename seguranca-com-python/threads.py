from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(2)
        print(f'Oiloto: {piloto}, km: {trajeto} \n')


t_carro1 = Thread(target=carro, args=[10, 'Bruno'])
t_carro2 = Thread(target=carro, args=[20, 'Python'])

t_carro1.start()
t_carro2.start()