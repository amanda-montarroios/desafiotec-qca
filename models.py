from pydantic import BaseModel, Field
from typing import List
from datetime import date


class Item(BaseModel):
    product_name: str
    quantity: int
    unit_price: float


class Invoice(BaseModel):
    order_id: int = Field(..., gt=0)
    order_date: date
    customer_id: str
    items: List[Item]

    @property
    def total_valor(self) -> float:
        return sum(item.quantity * item.unit_price for item in self.items)
