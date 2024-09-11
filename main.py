from fastapi import FastAPI
from api import auth
from api.routes import router as api_router


app = FastAPI()

app.include_router(auth.router)
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)