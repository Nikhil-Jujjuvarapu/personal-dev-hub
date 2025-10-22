import pandas as pd

def combine_two_tables(Person: pd.DataFrame, Address: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(Person, Address, on='personId', how='left')
    return merge_df[['firstName','lastName','city','state']]