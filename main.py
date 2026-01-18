import os
from ingestor import PDFIngestor
from repository import InvoiceRepository

DATA_FOLDER = "data/invoices"

def teste_ingestion_flow():
    """
    Script de teste para validar a extração e o armazenamento.
    """
    
    if not os.path.exists(DATA_FOLDER):
        print(f"Erro: A pasta {DATA_FOLDER} não existe. Crie ela e coloque os PDFs nela.")
        return

    ingestor = PDFIngestor()
    repo = InvoiceRepository(path="database.json")

    print("Iniciando processamento de PDFs...\n")

    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".pdf")]
    
    if not files:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return

    for filename in files:
        path = os.path.join(DATA_FOLDER, filename)
        print(f"Processando: {filename}...")
        
        try:
            invoice_data = ingestor.extrair_invoice(path)
            
            repo.salvar_invoice(invoice_data)
            
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")

    print("\nTeste concluído!")
    print(f"Verifique o arquivo 'database.json' para validar os dados.")

if __name__ == "__main__":
    teste_ingestion_flow()