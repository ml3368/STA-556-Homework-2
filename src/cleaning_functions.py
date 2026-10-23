import numpy as np
import pandas as pd




def remove_na(df):
    """Remove rows with missing values in the cnt, temp, or workingday columns

    Parameters
    ----
    df: pandas DataFrame
        raw data DataFrame to be cleaned
    
    Returns
    ----
    pandas DataFrame
        DataFrame with rows removed with missing values in the cnt, temp, or workingday columns
    """
    df_clean = df.dropna(subset = ["cnt", "temp", "workingday"])
    return(df_clean)

def select_cols(df):
    """Select columns of interest for analysis (cnt, temp, workingday)

    Parameters
    ----
    df: pandas DataFrame
        cleaned data to be filtered

    Returns
    ----
    pandas DataFrame
        DataFrame of all rows and only columns of interest
    """
    df_filtered = df[["cnt","temp","workingday"]]
    return(df_filtered)


def absolute_temp(df):
    """Change normalized temperature back to raw temps in Celsius with t_min is -8 C and t_max is 39 C

    Parameters
    ----
    df: pandas DataFrame
        filtered analysis data frame
    
    Retuns
    ----
    pandas DataFrame
        filtered analysis data frame with new abs_temp column
    """
    t_min = -8
    t_max = 39
    abs_temp = pd.Series([t_star*(t_max-t_min) + t_min for t_star in df["temp"]], name = "abs_temp")
    df_new = pd.concat([df, abs_temp], axis = 1)
    return(df_new)



def working_day(df):
    """Change binary work day/not work day to str representations of work day and not work day

    Parameters
    ----
    df: pandas DataFrame
        filtered analysis data frame with new abs_temp column
    
    Returns
    ----
    pandas DataFrame
        filtered analysis data frame with abs_temp column and new work_day column
    """
    work_day = pd.Series(("Work day" if x == 1 else "Not work day" for x in df["workingday"]), name = "work_day")
    df_new = pd.concat([df, work_day], axis = 1)
    return(df_new)



"""Classify a score as high or low using a threshold value

  Parameters
  ----
  score: float
    observed score to classify
  threshold: float, default = 80
    minimum value to define a score as high

  Returns
  ----
  str
    high if value is >= threshold
  """