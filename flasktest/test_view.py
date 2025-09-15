import pytest
from app import VALID_USERNAME, VALID_PASSWORD

def test_index_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Simple Flask Auth' in response.data  # Исправлено на актуальный текст

def test_dashboard_requires_login(client):
    """Тест что dashboard требует логина"""
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please log in first' in response.data  # Исправлено на актуальное сообщение
    assert b'Login' in response.data  # Должен быть редирект на логин

def test_dashboard_accessible_when_logged_in(client):
    """Тест доступа к dashboard после логина"""
    # Логинимся с правильными credentials
    client.post('/login', data={
        'username': VALID_USERNAME,  # Исправлено на актуальные данные
        'password': VALID_PASSWORD   # Исправлено на актуальные данные
    })

    # Затем получаем dashboard
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data
    assert b'admin' in response.data  # Исправлено на актуальное имя пользователя

def test_protected_route_redirects_to_login(client):
    """Тест что защищенные маршруты редиректят на логин"""
    response = client.get('/dashboard')
    assert response.status_code == 302  # Редирект
    assert '/login' in response.location  # Должен редиректить на логин
