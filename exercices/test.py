import pandas as pd

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def load_data(path : str):

    try : 
        df = pd.read_csv(path)
        logger.info ("Fichier chargé correctement !")
        return df
    except FileNotFoundError as e: 
        logger.error(f"Erreur dans le chargement du fichier")
        raise
    
    except Exception as e:
        logger.error(f"Unexpected error while loading data")
        raise


def validate_data(df:pd.DataFrame):

    errors = pd.DataFrame(index=df.index)

    errors['sale_id'] = df["sale_id"].isnull()
    errors['duplicate_sale_id'] = df["sale_id"].duplicated(keep=False)
    errors['product_id'] = df["product_id"].isnull()
    errors['quantity'] = df["quantity"] < 0
    errors['amount'] = df["amount"] <= 0

    sale_date_parsed = pd.to_datetime(df["sale_date"], errors="coerce")
    errors["invalid_sale_date"] = sale_date_parsed.isnull()

    invalid_mask = errors.any(axis=1)

    invalid_df = df[invalid_mask]
    valid_df = df[~invalid_mask]

    return invalid_df, valid_df

def compute_metrics(df:pd.DataFrame):

    cam = df.groupby("store_id").agg('sum')
    return cam


dn = load_data("sales.csv")
ivl, vl = validate_data(dn)

print("INVALID")
print(ivl)

print("#########################")
print("VALID")
print(vl.shape)

CA = compute_metrics(vl)
print(f"CA:{CA} ")

print("SORTED")
print(ivl.sort_values('amount'))
