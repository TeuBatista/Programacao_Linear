'''

Programação Linear e Otimização - Minimização do Custo (Modelo)
Autores:
Matheus Batista Silva
Felipe Daniel
Paulo Roberto

'''

#Importanto as bibliotecas necessárias
from setup import setup
from modelo import resolver
from obtencao_de_dados import obterDados

#Função principal: instalação de pacotes, obtenção de dados e resolução do problema
def main():

  #Instalando os pacotes necessários, caso estejam faltando
  setup()

  #Obtendo os dados necessários, gerados e armazenados nas planilhas
  professores, qnt_professores, disciplinas, qnt_disciplinas, arestas, custos = obterDados()

  #Resolvendo o problema com os dados obtidos
  resolver(professores, qnt_professores, disciplinas, qnt_disciplinas, arestas, custos)

if __name__ == "__main__":

  main()
