from fastapi import FastAPI
from app.routes import category
from fastapi.middleware.cors import CORSMiddleware

def create_application():
    application = FastAPI()
    application.include_router(category.category_router)
    return application

origins = [
    "http://localhost:3000", 
]


app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from these origins
    allow_credentials=True,  # Allows cookies to be sent in cross-origin requests
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers to be sent in requests
)


@app.get("/")
async def root():
    return {"message": "Hi, Your setup is done & working."}