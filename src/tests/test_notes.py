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
