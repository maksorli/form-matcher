import uvicorn
from fastapi import FastAPI

from app.db.database import init_db
from app.routes.form import router as form_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Form-matcher API"}


@app.on_event("startup")
async def startup():
    try:
        await init_db()
        print("Database connected successfully!")
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise e


app.include_router(form_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
