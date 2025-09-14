import pandas as pd

def collapse_flatlines(df, cols):
    """
    Collapse consecutive flatline values in specified columns of a DataFrame.
    
    A "flatline" is defined as consecutive identical values across the given columns.
    This function keeps the *first* occurrence in each flatline sequence and
    removes the repeated rows that follow, so the sequence is "collapsed" down.
    
    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame containing your data.
    cols : list of str
        The column names to check for flatlines (e.g., ['Flow_Rate', 'Pressure']).
        Flatline detection is based on *all* these columns being identical row-to-row.
    
    Returns
    -------
    pd.DataFrame
        A cleaned DataFrame where consecutive flatline rows are collapsed to the
        first occurrence only. The index from the original DataFrame is preserved.
    
    Example
    -------
    >>> df = pd.DataFrame({
    ...     'Flow_Rate': [5, 5, 5, 6, 7, 7, 8],
    ...     'Pressure':  [1, 1, 1, 2, 3, 3, 4]
    ... })
    >>> collapse_flatlines(df, ['Flow_Rate', 'Pressure'])
       Flow_Rate  Pressure
    0          5         1
    3          6         2
    4          7         3
    6          8         4
    """
    
    # Compare each row to the previous row across the specified columns.
    # If any column changes, we want to keep the row.
    mask = (df[cols] != df[cols].shift()).any(axis=1)
    
    # Always keep the very first row (index 0), even if it's part of a flatline.
    mask.iloc[0] = True
    
    # Apply the mask to keep the first row of each flatline sequence.
    return df[mask]
import numpy as np

""" USE THIS TO IMPORT AND TEST THE FUNCTION

from collapse_flatlines import collapse_flatlines

clean_df = collapse_flatlines(df, ['Flow_Rate', 'Pressure'])
print(clean_df)
"""  