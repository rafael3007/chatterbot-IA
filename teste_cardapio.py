import unittest
from robo import *

class TesteCardapio(unittest.TestCase):

    def setUp(self):
        #inicialização do robo
        self.robo = ChatBot("Robo de Atendimento Raff's",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])
        

    def testar_sobre_o_cardapio(self):
        mensagens = [ "cardápio", "qual o cardápio?","mande o cardápio","mande o cardápio, por favor","cardápio","me dê o cardápio","me dê o cardápio, por favor","cardapio, por favor" ],

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Temos:\n1) Coxinhas ( R$ 1,50 )\n2) Quibes ( R$ 1,00 )\n3) Pasteis de forno ( R$ 1,50 )\n4) Empadas ( R$ 1,00 )", resposta.text
            )
            
    def testar_sobre_a_coxinha(self):
        mensagens = ["a coxinha é de que?","tem coxinha de que?","tem coxinha de frango?"],

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A coxinha é de frango, temos com e sem catupiry.", resposta.text
            )
            
   
    
    def testar_sobre_a_empada(self):
        mensagens = ["a empada é de que?","tem empada de que?","tem empada de frango?"],

        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("A empada é de frango, temos de bacalhau mas ja acabou.", resposta.text)
            
            
    def testar_sobre_o_pastel_de_forno(self):
        mensagens = ["o pastel é de que?","tem pastel de que?","tem pastel de frango?","o pastel de forno é de que?","tem pastel de forno de que?","tem pastel de forno de frango?"],


        for mensagem in mensagens:
            resposta = self.robo.get_response(mensagem)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O pastel é de frango.", resposta.text
            )
    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteCardapio))

    executor = unittest.TextTestRunner()
    executor.run(testes)