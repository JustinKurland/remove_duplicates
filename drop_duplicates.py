import pandas as pd
import numpy as np
import pandas_flavor as pf

@pf.register_dataframe_method
def drop_duplicates(df):
    """
    Drop duplicated columns.
 
    Args:
         df ([pandas.DataFrame]):
          Dataframe of all columns to be evaluated.
    Output:
        df: dataframe with duplicated columns droppedd. 
            Note that the first evaluated column of a duplicate pair is kept.
    """
    print(f'Duplicate columns to be dropped:')

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
