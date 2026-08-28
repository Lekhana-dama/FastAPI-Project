from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

connected_clients = []


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    connected_clients.append(websocket)

    print("Client connected")

    try:
        while True:
            data = await websocket.receive_json()

            print("Received:", data)

            for client in connected_clients:
                await client.send_json(data)

    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Client disconnected")