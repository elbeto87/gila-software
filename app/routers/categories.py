from typing import List

from fastapi import APIRouter
from tinydb import Query

from app.database import categories_table
from app.schemas import CategoryModel
from app.utils import is_category_name_duplicated


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[CategoryModel])
def get_categories():
    return categories_table.all()


@router.post("/", response_model=CategoryModel)
def create_category(category: CategoryModel):
    is_category_name_duplicated(category.name)
    categories_table.insert(category.model_dump())
    return category


@router.delete("/{category_name}")
def delete_category(category_name: str):
    result = categories_table.get(Query().name == category_name)
    categories_table.remove(doc_ids=[result.doc_id])
    return {"message": "Category has been deleted"}
