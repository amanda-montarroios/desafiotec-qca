# Finance Invoice Processor 📊

Este projeto foi desenvolvido como parte de um desafio técnico para automação de processos financeiros. O sistema realiza a ingestão de faturas (invoices) em PDF, valida os dados utilizando **Pydantic**, armazena as informações em um banco local JSON e fornece insights analíticos através do **Pandas**.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13** (Versão do desafio)
- **Pydantic**: Validação de esquemas e integridade de dados.
- **Pandas**: Processamento e análise de dados.
- **pdfplumber**: Extração robusta de texto de arquivos PDF.
- **Orientação a Objetos**: Estrutura modular para separar as responsabilidades.

## 🏗️ Arquitetura do Projeto

O código foi estruturado seguindo o princípio de responsabilidade única:

* `models.py`: Definição dos schemas de dados (Invoice e Item).
* `ingestor.py`: Lógica de extração e parsing de arquivos PDF.
* `repository.py`: Gerenciamento do armazenamento local (JSON) e controle de duplicidade.
* `analytics.py`: Processamento analítico dos dados extraídos.
* `main.py`: Orquestrador do fluxo principal.



## 🚀 Como Executar o Projeto no VS Code

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local:

### 1. Clonar o Repositório
Abra o terminal do seu VS Code e utilize o comando:
```bash
git clone https://github.com/amanda-montarroios/desafiotec-qca

##Depois de clonar, escreva no terminal
python main.py

