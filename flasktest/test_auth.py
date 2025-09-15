import pytest
from app import VALID_USERNAME, VALID_PASSWORD

def test_index_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Simple Flask Auth' in response.data

def test_login_page(client):
    """Тест страницы логина"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'admin' in response.data  # prefilled username

def test_successful_login(client):
    """Тест успешного логина"""
    response = client.post('/login', data={
        'username': VALID_USERNAME,
        'password': VALID_PASSWORD
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Dashboard' in response.data
    assert b'Logged in successfully' in response.data

def test_failed_login_wrong_password(client):
    """Тест неудачного логина (неверный пароль)"""
    response = client.post('/login', data={
        'username': VALID_USERNAME,
        'password': 'wrongpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Invalid username or password' in response.data
    assert b'Login' in response.data  # Остаемся на странице логина

def test_failed_login_wrong_username(client):
    """Тест неудачного логина (неверный username)"""
    response = client.post('/login', data={
        'username': 'wronguser',
        'password': VALID_PASSWORD
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

def test_dashboard_requires_login(client):
    """Тест что dashboard требует логина"""
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please log in first' in response.data
    assert b'Login' in response.data  # Редирект на логин

def test_dashboard_accessible_when_logged_in(authenticated_client):
    """Тест доступа к dashboard после логина"""
    response = authenticated_client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data
    assert b'admin' in response.data

def test_logout(authenticated_client):
    """Тест логаута"""
    response = authenticated_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'You have been logged out' in response.data
    assert b'Welcome to Simple Flask Auth' in response.data  # Вернулись на главную

def test_session_cleared_after_logout(authenticated_client):
    """Тест что сессия очищается после логаута"""
    # Сначала проверяем что залогинены
    response = authenticated_client.get('/dashboard')
    assert response.status_code == 200

    # Логаутимся
    authenticated_client.get('/logout')

    # Пытаемся снова получить dashboard
    response = authenticated_client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please log in first' in response.data

def test_already_logged_in_redirect(client):
    """Тест редиректа если уже залогинен"""
    with client.session_transaction() as session:
        session['logged_in'] = True

    response = client.get('/login', follow_redirects=True)
    assert response.status_code == 200
    assert b'Dashboard' in response.data  # Редирект на dashboard
