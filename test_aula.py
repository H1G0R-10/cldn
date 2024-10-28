import pytest

@pytest.fixture

# Definido  uma fixture chamada 'lista_simples'
def lista_simples():
    return [1, 2, 3, 4, 5]

# Usando a fixture 'lista_simples' em um teste
def test_soma(lista_simples):
    assert sum(lista_simples)
    
def soma_dobro(numero):
    return sum(x * 2 for x in lista_simples)

    def testDobro(lista_simples):
 assert soma_dobro(lista_simples) == 15

    def names(nomes):
     return nomes[0]

     def tesNome(nomes):
      assert names(nomes) == "simnao" 
    
