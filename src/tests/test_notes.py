import json
import pytest
from app.notes.services import crud


def test_create_note(test_app, monkeypatch):
    test_request_payload = {"title": "something", "description": "something else"}
    test_response_payload = {
        "id": 1,
        "title": "something",
        "description": "something else",
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post(
        "/api/notes/",
        content=json.dumps(test_request_payload),
    )

    print(response.json())

    assert response.status_code == 201
    assert response.json()["title"] == test_response_payload["title"]
    assert response.json()["description"] == test_response_payload["description"]


def test_create_note_invalid_json(test_app):
    response = test_app.post("/api/notes/", content=json.dumps({"title": "something"}))
    assert response.status_code == 422


def test_read_note(test_app, monkeypatch):
    test_data = {
        "id": 18,
        "title": "something",
        "description": "something else",
    }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/api/notes/18")

    assert response.status_code == 200


def test_read_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.get("/api/notes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"


def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"title": "something", "description": "something else", "id": 1},
        {"title": "someone", "description": "someone else", "id": 2},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/api/notes/")
    assert response.status_code == 200
    # assert response.json() == test_data


def test_update_note(test_app, monkeypatch):
    test_update_data = {"title": "someone", "description": "someone else", "id": 3}

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 3

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/api/notes/3", content=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data


""" 
This test uses the pytest parametrize decorator to parametrize the arguments for the test_update_note_invalid function. 
"""


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"title": "foo", "description": "bar"}, 404],
    ],
)
def test_update_note_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(f"/api/notes/{id}/", content=json.dumps(payload))
    assert response.status_code == status_code


def test_remove_note(test_app, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 12}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return 12

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/api/notes/12/")
    assert response.status_code == 200
    # assert response.json() == test_data


def test_remove_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/api/notes/999/")

    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"
