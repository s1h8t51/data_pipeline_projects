import websocket
import json
from kafka import KafkaProducer

# Bybit public WebSocket for trades (BTCUSDT)
BYBIT_WS_URL = "wss://stream.bybit.com/v5/public/spot"

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def on_open(ws):
    print("WebSocket connection opened.")
    # Subscribe to BTCUSDT trade channel
    subscribe_msg = {
        "op": "subscribe",
        "args": ["publicTrade.BTCUSDT"]
    }
    ws.send(json.dumps(subscribe_msg))

def on_message(ws, message):
    msg = json.loads(message)
    # Filter only trade events
    if msg.get("topic") == "publicTrade.BTCUSDT":
        for trade in msg["data"]:
            print("Trade event:", trade)
            producer.send('crypto_trades', trade)

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed.")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        BYBIT_WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    print("Starting Bybit stream producer...")
    ws.run_forever()
