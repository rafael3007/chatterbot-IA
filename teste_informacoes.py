import unittest

from robo import *


class TesteInformacoes(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_horario(self):
        mensagens = [ "qual o horario de funcionamento?", "que horas voces ficam abertos?","ate horas voces ficam abertos?","ate horas voces funcionam?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
               "O estabelecimento, Raff's salgados, funciona pela noite, das 18:00 ate 00:00", resposta.text)

    def testar_tempo_de_preparo(self):
        mensagens = [ "qual o tempo de preparo?", "demora muito pra ficar pronto?", "vai demorar pra ficar pronto?","vai demorar para ficar pronto?","demora muito para ficar pronto?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O tempo medio de preparo e de 5minutos, ficara pronto em instantes, so um momento.", resposta.text)
            
            
    def testar_tempo_de_entrega(self):
        mensagens = [ "qual o tempo de entrega?", "demora muito pra chegar?", "demora muito para chegar?", "vai demorar pra entregar?", "vai demorar para entregar?"]
        
        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("A entrega varia de acordo a distancia, porem em media levamos 10 minutos para entregar o pedido", resposta.text)



if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)
