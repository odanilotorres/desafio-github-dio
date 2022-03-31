#Gerar, copiar, mover e escrever. Ler informaões de arquivos externos
import shutil


#criar e escrever no arquivo
# arquivo = open('teste.txt', 'a') #com o parametro w ele cria um novo arquivo, e com o parametro a ele atualiza o arquivo existente
# arquivo.write('\nMinha segunda escrita')
# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste2.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste2.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

#ler arquivos
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

# copiar arquivos
def copiar_arquivos(nome_arquivo):
    shutil.copy(nome_arquivo, 'diretorio desejado')


def mover_arquivos(nome_arquivo):
    shutil.move(nome_arquivo, 'diretorio desejado')


if __name__ == '__main__':
    #copiar_arquivos('nome_arquivo')
    #move_arquivos('nome_arquivo')
    # escrever_arquivo('Primeira linha\n')
    # atualizar_arquivo('Segunda linha\n')
    ler_arquivo('teste2.txt')
