import unittest
from src.base_code import Calculadora

class TestIntegracao(unittest.TestCase):
    
    def setUp(self):
        """Configuração executada antes de cada teste"""
        self.calc = Calculadora()
    
    # 4.1 Teste de Operações Sequenciais
    def test_operacoes_sequenciais(self):
        """Verificar se múltiplas operações funcionam em conjunto"""
        calc = Calculadora()
        # Sequência: 2 + 3 = 5, depois 5 * 4 = 20, depois 20 / 2 = 10
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()
        
        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()
        
        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()
        
        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)
    
    def test_operacoes_complexas(self):
        """Teste extra - sequÊncia de operações pt2"""
        calc = Calculadora()
        # Sequência: ((3^2) + 5) - 2 = 12
        calc.potencia(3, 2)  # 9
        resultado1 = calc.obter_ultimo_resultado()
        
        calc.somar(resultado1, 5)  # 14
        resultado2 = calc.obter_ultimo_resultado()
        
        calc.subtrair(resultado2, 2)  # 12
        resultado_final = calc.obter_ultimo_resultado()
        
        self.assertEqual(resultado_final, 12)
        self.assertEqual(len(calc.historico), 3)
    
    # 4.2 Teste de Interface entre Métodos
    def test_integracao_historico_resultado(self):
        """Verificar se diferentes métodos se comunicam corretamente"""
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10
        
        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ** 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)
    
    def test_integracao_limpar_historico(self):
        """Teste extra - integração com limpeza de histórico"""
        calc = Calculadora()
        calc.somar(5, 5)
        calc.multiplicar(calc.obter_ultimo_resultado(), 2)
        #op
        self.assertEqual(len(calc.historico), 2)
        self.assertEqual(calc.obter_ultimo_resultado(), 20)
        #clear
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
        self.assertEqual(calc.obter_ultimo_resultado(), 20)

if __name__ == '__main__':
    unittest.main()

"""
RELATÓRIO DE TESTES DE INTEGRAÇÃO

Execução dos Testes:
- Implementados 4 testes de integração
- Foco na comunicação entre métodos
- Validação de sequências de operações

Tipos de Teste Implementados:
1. Operações Sequenciais: Verificação de múltiplas operações em cadeia
2. Interface entre Métodos: Comunicação entre historico e resultado
3. Teste Extra - Operações Complexas: Sequências mais elaboradas
4. Teste Extra - Integração com Limpeza: Comportamento do sistema completo

Problemas Encontrados:
- Nenhum problema de integração identificado
- Métodos se comunicam corretamente
- Estado mantido consistente entre operações

"""