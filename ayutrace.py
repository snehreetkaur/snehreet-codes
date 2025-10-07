from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import qrcode
import os
import socket

app = FastAPI()

# In-memory database
db = {}

# Data model
class Batch(BaseModel):
    batch_id: str
    farmer: str
    harvest_date: str
    tests: str
    status: str

def get_host_ip():
    """Get local IP address for QR code generation."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

HOST_IP = get_host_ip()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Batch QR API!",
        "docs": f"http://{HOST_IP}:8000/docs",
        "example_add_batch": f"http://{HOST_IP}:8000/add_batch/"
    }

@app.post("/add_batch/")
def add_batch(batch: Batch):
    db[batch.batch_id] = batch.dict()

    # Generate QR code
    qr_url = f"http://{HOST_IP}:8000/get_batch/{batch.batch_id}"
    qr_img = qrcode.make(qr_url)

    os.makedirs("qrcodes", exist_ok=True)
    qr_path = f"qrcodes/{batch.batch_id}.png"
    qr_img.save(qr_path)

    print(f" QR Code generated: {qr_url}")

    return {
        "message": "Batch added successfully",
        "qr_code_path": qr_path,
        "access_url": qr_url
    }

@app.get("/get_batch/{batch_id}")
def get_batch(batch_id: str):
    if batch_id in db:
        return db[batch_id]
    raise HTTPException(status_code=404, detail="Batch not found")
@app.get("/get_batch/{batch_id}")
def get_batch(batch_id: str):
    if batch_id in db:
        return db[batch_id]
    raise HTTPException(status_code=404, detail="Batch not found")

@app.get("/qr/{batch_id}")
def get_qr_image(batch_id: str):
    qr_path = os.path.join(os.getcwd(), "qrcodes", f"{batch_id}.png")
    if os.path.exists(qr_path):
        return FileResponse(qr_path, media_type="image/png")
    raise HTTPException(status_code=404, detail="QR code not found")
if __name__ == "__main__":
    print(f" Server starting at: http://{HOST_IP}:8000")
    import uvicorn
    uvicorn.run("ayutrace:app", host="0.0.0.0", port=8000, reload=True)
