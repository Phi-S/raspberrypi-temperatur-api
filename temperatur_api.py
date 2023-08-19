# sudo apt install python3-pip python3-uvicorn python3-fastapi libgpiod2 && pip3 install adafruit-circuitpython-dht
# pip3 install adafruit-circuitpython-dht
import sys
import time
import board
import adafruit_dht
import uvicorn
from fastapi import FastAPI, HTTPException

port = 8001

dhtDevice = adafruit_dht.DHT22(board.D4)
dhtDevice.humidity
dhtDevice.temperature

app = FastAPI()

@app.get("/humidity")
def humidity_root():
    humidity = dhtDevice.humidity
    if humidity is None:
        raise HTTPException(status_code=500, detail="Failed to get valid humidity")
    return humidity

@app.get("/temperature")
def temperature_root():
    temperature = dhtDevice.temperature
    if temperature is None:
        raise HTTPException(status_code=500, detail="Failed to get valid temperature")
    return temperature

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
