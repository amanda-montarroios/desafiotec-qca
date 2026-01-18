import os
import pandas as pd

class InvoiceAnalytics:
    def __init__(self, path: str = "database.json"):
        if not os.path.exists(path):
                self.df = pd.DataFrame()
                self.items_df = pd.DataFrame()
                return
        self.df = pd.read_json(path)
      
        self.items_df = self.df.explode("items")
        self.items_df = pd.concat(
            [self.items_df.drop(["items"], axis=1),
             self.items_df["items"].apply(pd.Series)],
            axis=1
        )

        self.items_df["total"] = (
            self.items_df["quantity"] * self.items_df["unit_price"]
        )

    def media_invoice_valor(self):
        return self.df.apply(
            lambda x: sum(i["quantity"] * i["unit_price"] for i in x["items"]),
            axis=1
        ).mean()

    def mais_frequente_produto(self):
        return self.items_df["product_name"].value_counts().idxmax()

    def total_gasto_por_produto(self):
        return self.items_df.groupby("product_name")["total"].sum()

    def produto_list(self):
        return self.items_df[["product_name", "unit_price"]].drop_duplicates()
