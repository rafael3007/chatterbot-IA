import unittest
from robo import *

class TesteRecepcao(unittest.TestCase):

    def setUp(self):
        #inicialização do robo
        self.robo = iniciar()

    def testar_oi_ola(self):
        saudacoes = [ "oi", "ola" ]

        for saudacao in saudacoes:
            print(f"testando saudação {saudacao}")

            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Ola, sou o Raff's, um robo de atendimento. Como posso te ajudar?", 
                resposta.text
            )

    def testar_bom_dia_boa_tarde_boa_noite(self):
        saudacoes = ["bom dia", "boa tarde", "boa noite"]

        for saudacao in saudacoes:
            print(f"testando saudaçao {saudacao}")

            resposta = self.robo.get_response(saudacao.lower())
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                saudacao + ", sou o Raff's, um robo de atendimento. Como posso te ajudar?",
                resposta.text
            )


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteRecepcao))

    executor = unittest.TextTestRunner()
    executor.run(testes)