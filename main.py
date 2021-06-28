from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


@app.get("/connect")
def contact_details():
    return {"success": True}


@app.get("/hexapod/control")
def read_item(x: int = 0, y: int = 0, z: int = 0,
              roll: int = 0, pitch: int = 0, yaw: int = 0
              ):
    return {
        "success": True,
        "inputs": {'x': x, 'y': y, 'z': z,
                   "roll": roll, "pitch": pitch, "yaw": yaw}
    }
