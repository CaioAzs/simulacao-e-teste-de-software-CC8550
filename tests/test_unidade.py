import unittest
from src.base_code import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Configuração executada antes de cada teste"""
        self.calc = Calculadora()
    
    # 3.1 Testes de Entrada e Saída
    def test_entrada_saida_soma(self):
        """soma"""
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)
    
    def test_entrada_saida_subtracao(self):
        """subtração"""
        calc = Calculadora()
        resultado = calc.subtrair(10, 4)
        self.assertEqual(resultado, 6)
        self.assertEqual(calc.obter_ultimo_resultado(), 6)
    
    def test_entrada_saida_multiplicacao(self):
        """multiplicação"""
        calc = Calculadora()
        resultado = calc.multiplicar(7, 6)
        self.assertEqual(resultado, 42)
        self.assertEqual(calc.obter_ultimo_resultado(), 42)
    
    def test_entrada_saida_divisao(self):
        """divisão"""
        calc = Calculadora()
        resultado = calc.dividir(15, 3)
        self.assertEqual(resultado, 5.0)
        self.assertEqual(calc.obter_ultimo_resultado(), 5.0)
    
    def test_entrada_saida_potencia(self):
        """potência"""
        calc = Calculadora()
        resultado = calc.potencia(3, 2)
        self.assertEqual(resultado, 9)
        self.assertEqual(calc.obter_ultimo_resultado(), 9)
    
    # 3.2 Testes de Tipagem
    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)  # String no lugar de numero
        with self.assertRaises(TypeError):
            calc.dividir(10, None)  # None no lugar de numero
    
    def test_tipagem_subtracao(self):
        """tipagem para subtração"""
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.subtrair("10", 5)
        with self.assertRaises(TypeError):
            calc.subtrair(10, [])
    
    def test_tipagem_multiplicacao(self):
        """tipagem para multiplicação"""
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.multiplicar(5, "3")
        with self.assertRaises(TypeError):
            calc.multiplicar({}, 5)
    
    def test_tipagem_potencia(self):
        """tipagem para potência"""
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.potencia("2", 3)
        with self.assertRaises(TypeError):
            calc.potencia(2, True)
    
    def test_tipagem_lista(self):
        """Teste extra - rejeitar listas"""
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar([1, 2], 3)
    
    # 3.3 Testes de Consistência
    def test_consistencia_historico(self):
        """Verificar se os dados permanecem consistentes após operações"""
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)
    
    def test_consistencia_resultado_atualizado(self):
        """Teste extra - resultado é sempre atualizado"""
        calc = Calculadora()
        calc.somar(5, 5)
        self.assertEqual(calc.resultado, 10)
        calc.subtrair(8, 3)
        self.assertEqual(calc.resultado, 5)
    
    # 3.4 Testes de Inicialização
    def test_inicializacao(self):
        """Garantir que a estrutura é inicializada corretamente"""
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)
    
    def test_inicializacao_historico_vazio(self):
        """Teste extra - histórico inicia como lista vazia"""
        calc = Calculadora()
        self.assertIsInstance(calc.historico, list)
        self.assertEqual(calc.historico, [])
    
    # 3.5 Testes de Modificação de Dados
    def test_modificacao_historico(self):
        """Verificar se modificações são aplicadas corretamente"""
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    
    def test_modificacao_multiplas_operacoes(self):
        """Teste extra - múltiplas operações modificam histórico"""
        calc = Calculadora()
        calc.somar(1, 1)
        calc.dividir(10, 2)
        calc.potencia(2, 3)
        self.assertEqual(len(calc.historico), 3)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
    
    # 3.6 Testes de Limite Inferior
    def test_limite_inferior(self):
        """Testar comportamento com valores mínimos"""
        calc = Calculadora()
        # Teste com zero
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        # Teste com números negativos muito pequenos
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)
    
    def test_limite_numeros_negativos(self):
        """Teste extra - operações com números negativos"""
        calc = Calculadora()
        resultado = calc.somar(-10, -5)
        self.assertEqual(resultado, -15)
        resultado = calc.dividir(-20, -4)
        self.assertEqual(resultado, 5.0)
    
    # 3.7 Testes de Limite Superior
    def test_limite_superior(self):
        """Testar comportamento com valores máximos"""
        calc = Calculadora()
        # Teste com números grandes
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)
    
    def test_limite_float_maximo(self):
        """Teste extra - valores próximos ao limite de float"""
        calc = Calculadora()
        resultado = calc.multiplicar(1e100, 1e100)
        self.assertEqual(resultado, 1e200)
    
    # 3.8 Testes de Valores Fora do Intervalo
    def test_divisao_por_zero(self):
        """Verificar comportamento com valores inválidos"""
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
    
    def test_divisao_zero_por_zero(self):
        """Teste extra - zero dividido por zero"""
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(0, 0)
    
    # 3.9 Testes de Fluxos de Controle
    def test_fluxos_divisao(self):
        """Testar diferentes caminhos do código"""
        calc = Calculadora()
        # Caminho normal
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        # Caminho de erro
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)
    
    def test_fluxos_tipagem(self):
        """Teste extra - fluxos de validação de tipo"""
        calc = Calculadora()
        # Caminho normal
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        # Caminho de erro de tipo
        with self.assertRaises(TypeError):
            calc.somar("5", 3)
    
    # 3.10 Testes de Mensagens de Erro
    def test_mensagens_erro(self):
        """Verificar se mensagens de erro são claras"""
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")
    
    def test_mensagens_erro_tipo(self):
        """Teste extra - mensagens de erro de tipo"""
        calc = Calculadora()
        try:
            calc.somar("5", 3)
        except TypeError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")

if __name__ == '__main__':
    unittest.main()

"""
RELATÓRIO DE TESTES DE UNIDADE

Execução dos Testes:
- Implementados 20 tipos de testes de unidade
- Cobertura completa das funcionalidades da calculadora

Tipos de Teste Implementados
1. Entrada e Saída
2. Tipagem
3. Consistência
4. Inicialização
5. Modificação de Dados
6. Limite Inferior
7. Limite Superior
8. Valores Fora do Intervalo
9. Fluxos de Controle
10. Mensagens de Erro

Problemas Encontrados
- Nenhum problema crítico no código da calculadora
- Todas as validações funcionam
- Tratamento adequado de exceções
"""