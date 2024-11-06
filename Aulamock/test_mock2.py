import requests
import pytest 

# Função que faz uma chamada a uma API (apenas exemplo)

def obter_dados_da_api(url):
    resposta = requests.get(url)
    return resposta.json()

    # Teste sem fazer a chamada real à API

    def test_obter_dados_da_api(mocker):
        # Mockando a resposta da função requests.get
        mock_response = mocker.patch('requests.get')

        # Defindo um retorno ficticio para o mock
        mock_response.return_value.json.return_value = {"id": 1, "nome": "teste"}

        # Testando a função com o mock
        resultado = obter_dados_da_api("http://api.exemplo.com/dados")

        # Verificando se o resultado é o esperado
        assert resultado == {"id": 1, "nome": "Teste"}