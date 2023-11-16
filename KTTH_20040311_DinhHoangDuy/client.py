import asyncio
import websockets

async def get_weather(city):
    async with websockets.connect('ws://localhost:8765/weather') as websocket:
        await websocket.send(city)
        response = await websocket.recv()
        print(response)

city_name = input("Enter city name: ")
asyncio.get_event_loop().run_until_complete(get_weather(city_name))
