from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#think about this later
class User:
    def __init__(self):
        pass
    