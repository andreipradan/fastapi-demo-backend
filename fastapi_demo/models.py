import uuid
from typing import Optional

from edgedb import create_async_client
from pydantic import BaseModel


def get_fields(**kwargs):
    fields = kwargs.get('fields')
    return "{name, price, is_offer}" if not fields else ", ".join(kwargs['fields'])


class ItemManager:
    default_fields = ['id', 'name', 'price', 'is_offer']

    def __init__(self):
        self.client = create_async_client()
        self.fields = self.default_fields

    # async def get(self, **kwargs):
    #     query = f"select Item {get_fields(**kwargs)}"
    #     if 'q' in kwargs:
    #         query += f" filter .name ilike '%{kwargs['q']}%'"
    #     print(query)
    #     response = await self.client.query_single(query)
    #     self.client.aclose()
    #     return PydanticItem.from_orm(await response)

    async def create(self, **kwargs):
        insert_str = "insert Item {{{}}}"
        insert_components = []
        if "name" in kwargs:
            insert_components.append("name:=<str>$name")
        if "price" in kwargs:
            insert_components.append("price:=<float32>$price")
        if "is_offer" in kwargs:
            insert_components.append("is_offer:=<bool>$is_offer")
        item = await self.client.query(
            insert_str.format(", ".join(insert_components)), **kwargs
        )
        return PydanticItem.from_orm(item[0])

    async def delete(self, item_id):
        delete_str = f"delete Item filter .id=<uuid>'{item_id}'"
        item = await self.client.query(delete_str)
        return PydanticItem.from_orm(item[0])

    def only(self, fields):
        self.fields = fields
        return self

    async def search(self, q):
        query = self.select_str
        if q:
            query += " filter .name ilike '%{q}%'"
        results = await self.client.query(query)
        return [PydanticItem.from_orm(i).dict(exclude_unset=True) for i in results]

    @property
    def select_str(self):
        return f"select Item {{{', '.join(self.fields)}}}"


class Item:
    objects = ItemManager()


class PydanticItem(BaseModel):
    id: uuid.UUID
    name: Optional[str]
    price: Optional[float]
    is_offer: Optional[bool] = None

    class Config:
        orm_mode = True
