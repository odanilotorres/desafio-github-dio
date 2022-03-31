# aprendendo a manipular data, horrio e relacionar datas diferentes

from datetime import date, datetime #importanto a funcao date

def trabalhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_datetime():
    time_atual = datetime.now()
    print(time_atual.time())
    tupla = ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[time_atual.weekday()])


if __name__ == '__main__':
    #trabalhando_date()
    trabalhando_com_datetime()