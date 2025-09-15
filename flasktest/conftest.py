import pytest
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        'TESTING': True,
        'SECRET_KEY': 'test-secret-key'
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def authenticated_client(client):
    # Автоматически логинимся для тестов, требующих аутентификации
    with client.session_transaction() as session:
        session['logged_in'] = True
        session['username'] = 'admin'
    return client
