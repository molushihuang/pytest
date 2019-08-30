import requests

url = 'http://echo.websocket.org/?encoding=text'
header = {
    "Host": "echo.websocket.org",
    "Upgrade": "websocket",
    "Connection": "Upgrade",
    "Sec-WebSocket-Key": "9GxOnSwEuBNbLeBwiltymg==",
    "Origin": "http://www.websocket.or",
    "Sec-WebSocket-Protocol": "chat, superchat",
    "Sec-WebSocket-Version": "13"
}

resp = requests.get(url, headers=header)
print(resp.status_code)
