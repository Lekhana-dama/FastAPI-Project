from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({
            "message": "Hello"
        })

        data = websocket.receive_json()

        assert data["message"] == "Hello"