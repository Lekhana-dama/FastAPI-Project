import websocket
import json

ws = websocket.create_connection("ws://127.0.0.1:8000/ws")

print("Connected to WebSocket!")

message = {
    "username": "Bob",
    "message": "Hello FastAPI!"
}

ws.send(json.dumps(message))

print("Message sent!")

response = ws.recv()

print("Server response:")
print(response)

ws.close()