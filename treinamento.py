from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSAS = [
    "C:/Users/Rafael/Desktop/chatterbot/Avaliação_II/chatterbot-IA/conversas/cardapio.json",
    "C:/Users/Rafael/Desktop/chatterbot/Avaliação_II/chatterbot-IA/conversas/informacoes.json",
    "C:/Users/Rafael/Desktop/chatterbot/Avaliação_II/chatterbot-IA/conversas/recepcao.json",
]

def iniciar():
    robo = ChatBot("Robô de Atendimento Raff's")
    treinador = ListTrainer(robo)

    return treinador

def carregar_conversas():
    conversas = []

    #pega todos os arquivos de conversa
    for arquivo_conversas in CONVERSAS:
        with open(arquivo_conversas, "r") as arquivo:
            conversas_para_treinamento = json.load(arquivo)
            conversas.append(conversas_para_treinamento["conversas"])

            #tem que fechar o arquivo
            arquivo.close()

    return conversas

def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            #mensagem para acompanhar o Treinamento do robo
            print(f"treinando o robô. Mensagens: {mensagens}. Resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])


def inicializar_treinamento_do_robo():
    treinador = iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar(treinador, conversas)

if __name__ == "__main__":
    treinador = iniciar()

    conversas = carregar_conversas()
    
    #se tiver conversas treine
    if conversas:
        treinar(treinador, conversas)
