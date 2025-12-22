import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

df = pd.read_csv("client.csv", sep=',')

# def validate_data(df : pd.DataFrame): 
#     #Enlever les doublons
#     df = df.drop_duplicates()

#     errors = pd.Series(False, index=df.index)
#     mandatory_cols = ["campaign_id", "store_id", "product_id"]

#     #Ces trois colonnes sont nuls --> erreur
#     for col in mandatory_cols:
#         errors |= df[col].isnull()

#     #impression est nul ou < 0
#     errors |= df["impressions"].isnull()
#     errors |= df["impressions"] < 0

#     #sales_amount <=0
#     errors |= df["sales_amount"] <= 0

#     #event_date n'est pas une date valide

#     df["event_date_parsed"] = pd.to_datetime(
#         df["event_date"], errors="coerce"
#     )

#     errors |= df["event_date_parsed"].isnull()
#     invalid_df = df[errors]
#     valid_df = df[~errors].drop(columns=df["event_date_parsed"])
#     return valid_df, invalid_df

# # valid_df = df[~errors].drop(columns=df["event_date_parsed"])

# # print(valid_df)

#1. Lire le fichier ccv
df=pd.read_csv("sales.csv", sep=(','))

errors = pd.DataFrame(index=df.index)

#sale_id is not null
errors["invalid_sale_id"] = df["sale_id"].isnull()
#sale_id is unique
errors["duplicate_sale_id"] = df["sale_id"].drop_duplicates(keep=False)

#product_id non nul
errors["product_id"] = df["product_id"].isnull()

errors["quantity"] = df["quantity"] <=0

errors["amount"] = df["amount"] <=0

errors["sale_date"] = df["sale_date"]

# invalid = df[errors]

print("Dataframe")
print(df)
print("Valid ! ")
print(errors)



print(errors)

# def validate_data(df:pd.DataFrame):
#     logging.info("Inititing data validation !")
    
#     #2. Appliquer les règles de qualité
#         #sale_id unique et non nul

#    

#     #product_id non nul
#     df["product_id"] !=0

#     #quantity > 0

#     df["quantity"] > 0
#     #amount > 0

#     df["amount"] > 0

#     #sale_date au format valide
#     df["sale_date"] = df["sale_date"].to_datetime()
    #3. Gérer les erreurs
    #Séparer les lignes invalides des lignes valides
    #Logger les erreurs
    # 4.Produire un output
    #Calculer le chiffre d’affaires par magasin
    #Sauvegarder le résultat dans un fichier CSV



