import pandas as pd
import numpy as np
import pandas_flavor as pf

@pf.register_dataframe_method
def remove_duplicates(df):
    """
    Remove duplicated columns.
 
    Args:
         df ([pandas.DataFrame]):
            Dataframe of all columns to be evaluated.
    Returns:
        df ([pandas.DataFrame]): Dataframe with duplicated columns dropped. 
        Note that the first evaluated column of a duplicate is kept.
    """
    print(f'Duplicate columns to be removed:')

    nums = df._get_numeric_data().columns.tolist()
    df_num = df[nums].astype(float)
    df_str = df[df.columns.difference(nums)]
    df = pd.concat([df_num,df_str], axis=1)
    dupe_cols = []

    for i in range(len(df.columns)):
        col_1 = df.columns[i]
        if col_1 not in dupe_cols:
            for col_2 in df.columns[i + 1:]:
                if df[col_1].equals(df[col_2]):
                    dupe_cols.append(col_2)
                    print(f'\t{col_2}')
 
    df = df.drop(dupe_cols, axis=1)
    
    return df
