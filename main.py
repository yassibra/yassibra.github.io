from fastapi import FastAPI

app = FastAPI()
token = "mytoken"

@app.get("/")
async def root():
    return {"message": "Hello worlda"}

@app.get("/callback")
async def root():
    return {"token": token}