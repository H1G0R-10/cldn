import pytest
from unittest import mock
from sua_aplicacao import calcular_valor_total, BancoDeDados, obter_pedido_com_valor_total  # Substitua com o nome correto do arquivo

# Teste para calcular o valor total de um pedido
def test_calcular_valor_total(mocker):
    mock_resposta = mock.Mock()
    mock_resposta.json.return_value = [
        {"preco": 100, "quantidade": 2},
        {"preco": 50, "quantidade": 1}
    ]
    
    mocker.patch("requests.get", return_value=mock_resposta)
    
    pedido_id = 1
    valor_total = calcular_valor_total(pedido_id)
    
    assert valor_total == 250  # (100*2 + 50*1)

# Fixture para simular o banco de dados
@pytest.fixture
def banco_mock():
    banco = mock.Mock()
    banco.buscar_pedido.return_value = {"id": 1, "cliente": "João"}
    return banco

# Teste para obter o pedido com o valor total
def test_obter_pedido_com_valor_total(banco_mock, mocker):
    mock_resposta = mock.Mock()
    mock_resposta.json.return_value = [
        {"preco": 100, "quantidade": 2},
        {"preco": 50, "quantidade": 1}
    ]
    
    mocker.patch("requests.get", return_value=mock_resposta)
    
    pedido_id = 1
    pedido_com_valor_total = obter_pedido_com_valor_total(pedido_id, banco_mock)
    
    assert pedido_com_valor_total["valor_total"] == 250  # (100*2 + 50*1)
    assert pedido_com_valor_total["id"] == 1
    assert pedido_com_valor_total["cliente"] == "João"
