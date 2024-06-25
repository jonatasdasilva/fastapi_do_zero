from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.server import server


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(server)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK   # Assert
    assert response.json() == {'message': 'Olá Mundo!'}
