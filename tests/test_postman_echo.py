import requests

def test_get_request():
    """Тест 1: GET-запрос с параметрами"""
    url = "https://postman-echo.com/get"
    params = {"name": "Alice", "age": 25}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.json()["args"]["name"] == "Alice"
    assert response.json()["args"]["age"] == "25"

def test_post_json():
    """Тест 2: POST-запрос с JSON"""
    url = "https://postman-echo.com/post"
    data = {"key": "value", "number": 123}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()["json"] == data

def test_post_form():
    """Тест 3: POST-запрос с формой (form-data)"""
    url = "https://postman-echo.com/post"
    form_data = {"username": "testuser", "password": "12345"}
    response = requests.post(url, data=form_data)
    assert response.status_code == 200
    assert response.json()["form"]["username"] == "testuser"

def test_put_request():
    """Тест 4: PUT-запрос"""
    url = "https://postman-echo.com/put"
    data = {"message": "hello world"}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json()["json"]["message"] == "hello world"

def test_delete_request():
    """Тест 5: DELETE-запрос"""
    url = "https://postman-echo.com/delete"
    response = requests.delete(url)
    assert response.status_code == 200