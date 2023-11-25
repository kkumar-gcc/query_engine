from fastapi import APIRouter
from openai import OpenAI
from chromo.client import chroma_collection
from config import OPENAI_API_KEY

router = APIRouter()

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def build_prompt(product_query: str, references: list) -> tuple[str, str]:
    prompt = f"""
    Product Information Request:

    Search the vector database for detailed information about the product with the following query:

    '{product_query}'

    References:
    """.strip()

    references_text = ""
    print(references)
    for i, reference in enumerate(references.documents, start=1):
        print(i, reference)
        text = reference.strip()
        references_text += f"\n[{i}]: {text}"

    prompt += f"""
    '{references_text}'
    
    Provide a comprehensive response based on the available data. Include key details, specifications, and any noteworthy information regarding '{product_query}'. 
    If possible, cite relevant sources using references [1], [2], etc.

    Response:
    """

    return prompt, references_text


@router.get("/search")
async def search(query: str):
    # Search for the most similar vectors
    search_results = chroma_collection.query(
        query_texts=[query]
    )

    prompt, references = build_prompt(query, search_results)

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
        max_tokens=250,
        temperature=0.1,
    )

    return {
        "response": response.choices[0].message.content,
        "references": references,
    }
