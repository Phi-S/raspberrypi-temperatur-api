# sudo apt install python3-pip python3-uvicorn python3-fastapi libgpiod2 && pip3 install adafruit-circuitpython-dht
# pip3 install adafruit-circuitpython-dht
import sys
import time
import board
import adafruit_dht
import uvicorn
from fastapi import FastAPI, HTTPException, Response

port = 8001
app = FastAPI()


@app.get("/")
def temperature_root():
    for i in range(10):
        try:
            dht_device = adafruit_dht.DHT22(board.D4)
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            if ((isinstance(temperature, int) or isinstance(temperature, float))
                    and -10 < temperature < 60 and
                    (isinstance(humidity, int) or isinstance(humidity, float))
                    and 0 < humidity <= 100):
                return {"temperature": temperature, "humidity": humidity}
            else:
                print("Not an int or float. retry")
                continue
        except Exception:
            print("retry")
            continue
    else:
        return Response(status_code=500)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
