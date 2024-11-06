import pytest
import requests
from unittest.mock import MagicMock

@pytest.fixture
def mock_responde():
    #simulando uma chamada de API
    mock = MagicMock(spec=requests.Responde)
    mock.status_code = 200
    mock.json.return_value = {"massege" : "sucess"}
    return mock

    def test_api_chamnada_com_mock(mock_responde):
        #Definindo um retorno para mock
        response = mock_responde
        assert response.status_code == 200
        assert response.json() == {"massege": "sucess"}