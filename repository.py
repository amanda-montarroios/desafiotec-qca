import json
import os
from typing import List
from models import Invoice


class InvoiceRepository:
    def __init__(self, path: str = "database.json"):
        self.path = path

    def load(self) -> List[dict]:
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar_invoice(self, invoice: Invoice):
        data = self.load()

        if any(inv["order_id"] == invoice.order_id for inv in data):
            print(f"Invoice {invoice.order_id} já existe. Ignorada.")
            return

        data.append(invoice.model_dump(mode="json")) 

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Invoice {invoice.order_id} salva com sucesso.")