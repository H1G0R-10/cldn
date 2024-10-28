import pytest

@pytest.fixture
def setup():
    # Configuração para os testes, se necessário
    pass

def acordar_cedo(horario):
    if horario > 6:
        return 'Tente novamente amanhã'
    return 'Você é um guerreiro'

def tempo_exercicio(peso, tempo):
    if tempo > 2:
        peso -= 1
        return peso
    return peso  # Retorna o peso original se o tempo for menor ou igual a 2

def tem_exercicio(esporte):
    if esporte == 'Descanso':
        return False
    return True

# Aqui você pode adicionar testes com pytest
def test_acordar_cedo():
    assert acordar_cedo(7) == 'Tente novamente amanhã'
    assert acordar_cedo(6) == 'Você é um guerreiro'

def test_tempo_exercicio():
    assert tempo_exercicio(10, 3) == 9
    assert tempo_exercicio(10, 1) == 10

def test_tem_exercicio():
    assert tem_exercicio('Futebol') == True
    assert tem_exercicio('Descanso') == False
