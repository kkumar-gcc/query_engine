from fastapi import APIRouter

router = APIRouter()


def build_prompt(product_query: str, references: list) -> tuple[str, str]:
    pass


@router.get("/search")
async def search(query: str):
    pass
