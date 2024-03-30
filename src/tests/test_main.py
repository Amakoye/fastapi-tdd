def test_ping(test_app):
    response = test_app.get("/api/test/test-api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello there"}


def test():
    assert 22 == 22
