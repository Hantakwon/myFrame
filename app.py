from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# 앱 설정
app = FastAPI()

# 앱 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/")
async def root():
    return {"message": "Hello World"}

@app.delete("/")
async def root():
    return {"message": "Hello World"}

items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=418, detail="I'm teapot")
    return {"item": items[item_id]}