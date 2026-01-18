import pdfplumber
import re
from models import Invoice, Item
from datetime import datetime


class PDFIngestor:

    def extrair_invoice(self, pdf_path: str) -> Invoice:
        with pdfplumber.open(pdf_path) as pdf:
            text = pdf.pages[0].extract_text()

        order_id = int(re.search(r"Order ID:\s*(\d+)", text).group(1))
        customer_id = re.search(r"Customer ID:\s*(\w+)", text).group(1)
        order_date_str = re.search(r"Order Date:\s*(\d{4}-\d{2}-\d{2})", text).group(1)
        order_date = datetime.strptime(order_date_str, "%Y-%m-%d").date()

        items = []
        lines = text.splitlines()

        for line in lines:
            match = re.match(r"\d+\s+(.+?)\s+(\d+)\s+([\d.]+)", line)
            if match:
                items.append(
                    Item(
                        product_name=match.group(1),
                        quantity=int(match.group(2)),
                        unit_price=float(match.group(3))
                    )
                )

        return Invoice(
            order_id=order_id,
            order_date=order_date,
            customer_id=customer_id,
            items=items
        )