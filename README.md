# Relatório de Testes - Calculadora

## Resultado da Execução dos Testes

### Status Geral
- **Total de testes executados**: 30 testes
- **Testes aprovados**: 29 testes
- **Testes falharam**: 1 teste

### Falha Identificada

#### Teste de Tipagem - Potência
**Arquivo**: `test_unidade.py`  
**Método**: `test_tipagem_potencia`  
**Linha**: 75  
**Erro**: `AssertionError: TypeError not raised`  
**Código problemático**:
```python
with self.assertRaises(TypeError):
    calc.potencia(2, True)  # Esperava TypeError mas não foi gerado
```

**Causa**: Em Python, o tipo `bool` é um subtipo de `int`. Portanto:
- `isinstance(True, (int, float))` retorna `True`
- `True` é automaticamente convertido para `1` em operações matemáticas

## Cobertura de Código

### Detalhamento por Arquivo
| Arquivo | Linhas | Miss | Cobertura |
|---------|--------|------|-----------|
| `src/calculadora.py` | 46 | 0 | 100% |
| `tests/test_unidade.py` | 148 | 1 | 99% |
| `tests/test_integracao.py` | 45 | 1 | 98% |

## Problemas Encontrados e Soluções

### Problema: Validação de Tipos Boolean

**Descrição Técnica:**
O teste `test_tipagem_potencia` espera que `calc.potencia(2, True)` gere um `TypeError`, mas isso não acontece porque:

1. Python trata `bool` como subtipo de `int`
2. A validação atual usa `isinstance(valor, (int, float))`
3. `isinstance(True, int)` retorna `True`
4. Portanto, `True` é aceito como parâmetro válido

**Solução:**

#### Alteração na validação a Calculadora
Rejeitar tipos boolean:
```python
def potencia(self, base, expoente):
    if (not isinstance(base, (int, float)) or isinstance(base, bool) or not isinstance(expoente, (int, float)) or isinstance(expoente, bool)):
        raise TypeError("Argumentos devem ser numeros")
```

#### Categoria com Problema:
- **Tipagem**: 4/5 aprovados - falha na validação de boolean

## Lições Aprendidas

### Sobre Tipagem em Python:
- `bool` é subtipo de `int` - comportamento fundamental da linguagem
- Testes devem considerar hierarquia de tipos do Python
- Validação de tipos requer conhecimento das especificidades da linguagem

### Resultados Atuais:
- **Taxa de Sucesso**: 96,67% (29/30 testes)
- **Cobertura de Código**: 99%
- **Tempo de Execução**: 0.004s

### Avaliação da Qualidade:
- **Calculadora**: Funcionamento perfeito (100% cobertura)
- **Testes**: Abrangentes e bem estruturados
- **Única questão**: Validação de tipos

## Conclusão

- Necessário tratamento adequado de exceções em relação a tipagem
