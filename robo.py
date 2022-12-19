from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.4


def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, 
            digitada,
            candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca

def iniciar():
    robo = ChatBot("Robô de Atendimento Raff's",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo


def executar_robo(robo):
    while True:
        mensagem = input("Raff's:Eu me chamo Raff's e irei te auxliar hoje! Como posso te ajudar?. \n")
        resposta = robo.get_response(mensagem.lower())
        #print(f"o valor da confiança é: {resposta.confidence}")
        if resposta.confidence >= CONFIANCA_MINIMA:
            print("Raff's>>", resposta.text)
        else:
            print("Raff's: Infelizmente, ainda não sei responder isso")
            print("Raff's: Pergunte outra coisa")


def inicializar():
    robo = iniciar()
    executar_robo(robo) 
    
    
    
if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)
