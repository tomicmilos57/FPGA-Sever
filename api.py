import tempfile
from fastapi import FastAPI, Request
import subprocess

app = FastAPI()


@app.get("/ping")
async def ping():
    print("pong")
    return {"message": "pong"}


@app.post("/sof")
async def sof(request: Request):
    binary = await request.body()

    with tempfile.NamedTemporaryFile(suffix=".sof", delete=False) as tmp:
        tmp.write(binary)
        tmp_path = tmp.name

    pgm = subprocess.run(
        [
            "/home/milos/.wine/drive_c/altera/13.1/quartus/bin/quartus_pgm.exe",
            "--mode=JTAG",
            f"--operation=P;{tmp_path}"
        ],
        capture_output=True
    )
    print(pgm)
    return {"message": len(binary)}

if __name__ == "__main__":
    uvicorn.run("example:app", host="127.0.0.1", port=5000, reload=True)
