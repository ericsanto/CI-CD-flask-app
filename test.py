import pytest
from flask import Flask

# Supondo que o seu app esteja em um arquivo chamado app.py
from app import app  # Altere "app" para o nome do seu arquivo, se necessário

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello. Iam FLask'
    assert response.status_code == 200


def test_teste(client):
    response = client.get('/testeab')
    assert response.data == b'Essa. e uma pagina para teste'
    assert response.status_code == 200