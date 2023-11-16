import asyncio
import websockets
import json
import requests

# Các thông tin cấu hình của OpenWeather API
api_key = 'da6c03b7e8178e5a82ce909cf7a92078'

# Định nghĩa hàm để lấy thông tin thời tiết từ OpenWeather API cho 8 ngày
def get_8_day_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()
    
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def get_map():
    url=f'https://maps.openweathermap.org/maps/2.0/weather/1h/TA2/4/1/6?appid={api_key}'
    response = requests.get(url)
    return response.json()
# Hàm xử lý kết nối từ client
async def handle_connection(websocket, path):
    while True:
        city = await websocket.recv()
        if path=="/forescast":
            weather_data = get_8_day_forecast(city)
            await websocket.send(json.dumps(weather_data))
        if path=="/weather":
            weather_data1 = get_weather(city)
            await websocket.send(json.dumps(weather_data1))
        if path=="/map":
            weather_data2 = get_map(city)
            await websocket.send(json.dumps(weather_data2))
# Khởi tạo server WebSocket
start_server = websockets.serve(handle_connection, "localhost", 8765)

# Chạy server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
