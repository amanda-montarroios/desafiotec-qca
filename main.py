import os
from ingestor import PDFIngestor
from repository import InvoiceRepository
from analytics import InvoiceAnalytics


PDF_FOLDER = "data/invoices"

def main():
    ingestor = PDFIngestor()
    repo = InvoiceRepository()

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            invoice = ingestor.extrair_invoice(
                os.path.join(PDF_FOLDER, file)
            )
            repo.salvar_invoice(invoice)

    analytics = InvoiceAnalytics()

    print("\nANALYTICS")
    print("Média do valor das faturas:", analytics.media_invoice_valor())
    print("Produto mais comprado:", analytics.mais_frequente_produto())
    print("\nTotal gasto por produto:")
    print(analytics.total_gasto_por_produto())
    print("\nLista de produtos:")
    print(analytics.produto_list())


if __name__ == "__main__":
    main()
