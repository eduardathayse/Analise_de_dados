"""
Análise de dados para empresas

Desafio:
Uma empresa de telecom tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com 
Churn de mais de 26% dos clientes. Isso representa uma perda de milhões para a empresa.
(Churn en termos gerais é quando clientes não renovam contratos - https://resultadosdigitais.com.br/blog/o-que-e-churn/)


Base de dados obtida do kaggle (Plataforma de aprendizagem e competição para cientistas de dados)
Link Original da base de dados do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset
"""
# importando bibliotecas 
import pandas as pd
import plotly.express as px # pip install plotly -> biblioteca para criar gráficos

class RoboAnaliseDados:
    
    def __init__(self):
        self.tabela_clientes = ''

    def importar_visualizar_tabela(self):
        """ Importar e visualizar a base de dados """

        self.tabela_clientes = pd.read_csv('telecom_users.csv') # armazenando arquivo csv em uma variavel
        self.tabela_clientes = self.tabela_clientes.drop(["Unnamed: 0"], axis=1) # apagando a coluna Unnamed: 0, axist=1 -> para excluir a coluna, axist=0 -> excluir a linha  (exist = eixo)
        print(self.tabela_clientes)
        # print(self.tabela_clientes.columns) # para mostrar todas as colunas da tabela 
        self.tabela_clientes['NovaColuna'] = 1 # criar uma nova coluna se não existir, se caso ja exista, irá substituir todos os valores na coluna para 1

    def Tratamentos_dos_dados(self):  
        """ Tratamentos dos dados da tabela (Ajeitar Problemas da Base de Dados)
        
        Obrigatoriamente nessa ordem:
        . Tratar valores de "tipo" errado
        . Trata valores vazios 
        """
        self.tabela_clientes["TotalGasto"] = pd.to_numeric(self.tabela_clientes["TotalGasto"], errors="coerce") # transformar coluna que deveria ser número e está como texto em número,  errors="coerce" -> se der erro em algo deixa vazio
        
        self.tabela_clientes = self.tabela_clientes.dropna(how='all', axis=1) # remover as colunas que estam 100% vazia,  how='all' -> todas
        
        self.tabela_clientes = self.tabela_clientes.dropna() # remover a linha que tem algum valor vazio

        print(self.tabela_clientes.info()) # informações sobre a tabela 

    def Churn(self):
        """ Visão geral de como estão distribuidos dos os churns/cancelamentos """

        print(self.tabela_clientes['Churn'].value_counts()) # contando os valores da tabela Churn (quantidade sim e não)
        print(self.tabela_clientes['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) #  contando os valores da tabela Churn (quantidade sim e não) e mostrando o percentual e formatando com o .map

    def Analise_do_churn(self):
        """ Analisar as causas dos cancelamentos 
        
        
        """
        # grafico = px.histogram(self.tabela_clientes, x='Churn', color='Churn') # criando gráfico da tabela clientes onde o eixo x tem as informações de churn com cores diferentes
        # grafico.show() # exibe o grafico
        # # para edições nos gráficos: https://plotly.com/python/histograms/
        
        
        # for coluna in self.tabela_clientes.index: # index para percorrer as linhas 
        for coluna in self.tabela_clientes: # para percorrer as colunas
            if coluna != "IDCliente":
                # criar a figura
                fig = px.histogram(self.tabela_clientes, x=coluna, color="Churn")
                # exibir a figura
                fig.show()
                print(self.tabela_clientes.pivot_table(index="Churn", columns=coluna, aggfunc='count')["IDCliente"])

""" ============== Main ============== """
robo = RoboAnaliseDados()
robo.importar_visualizar_tabela()
robo.Tratamentos_dos_dados()
robo.Churn()
robo.Analise_do_churn()

import os
os.system('pause')

