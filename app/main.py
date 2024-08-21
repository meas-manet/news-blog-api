from fastapi import FastAPI
from app.routes import category

def create_application():
    application = FastAPI()
    application.include_router(category.category_router)
    return application


app = create_application()


@app.get("/")
async def root():
    return {"message": "Hi, Your setup is done & working."}