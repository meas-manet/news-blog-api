from fastapi import APIRouter

category_router = APIRouter(prefix="/Category/api", tags=["Category"])

@category_router.get("/")
def get_all_categories():
    return "Not Implemented"

@category_router.post("/")
def create_category():
    return "Not Implemented"

@category_router.put("/{id}")
def update_category(id:int):
    return "Not Implemented"

@category_router.delete("/{id}")
def delete_category(id:int):
    return "Not Implemented"