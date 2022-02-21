import os
import uuid
from typing import Optional

import edgedb
import uvicorn
from fastapi import FastAPI, Query, HTTPException, Form, status

from fastapi_demo.models import Item, PydanticItem

app = FastAPI()


@app.get("/")
async def home():
    return {"hello": "world"}


@app.get("/api/")
async def api(q: Optional[str] = None, field: list[str] | None = Query(None)):
    qs = Item.objects
    if field:
        qs = qs.only(field)
    return await qs.search(q)


@app.post("/api/", status_code=status.HTTP_201_CREATED)
async def add_item(
        name: str = Form(...),
        price: float = Form(...),
        is_offer: bool = Form(False)
) -> PydanticItem:
    try:
        return await Item.objects.create(name=name, price=price, is_offer=is_offer)
    except edgedb.errors.ConstraintViolationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/api/items/{item_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: uuid.UUID):
    await Item.objects.delete(item_id)


def start():
    uvicorn.run(
        "fastapi_demo.main:app",
        host="0.0.0.0",
        port=int(os.environ["PORT"]),
    )
