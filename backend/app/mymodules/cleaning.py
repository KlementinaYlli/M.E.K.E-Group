"""
Cleaning module.

Contains functions for cleaning.
"""

import pandas as pd


def load_and_clean_data(file_path):
    """
    Loas and cleans a csv file.

    Args:
        file_path (str): path of the file

    Returns:
        Dataframe | None: Cleaned data
    """

    # Loads and cleans data
    # sep=; means that ";" is used as a separator instead of ","
    data = pd.read_csv(file_path, sep=';')
    columns_to_drop = ["Codice Plesso Scolastico", "Codice Edificio", "Edifici Attivo (SI-NO)", "Codice Istituzione Scolastica", "Codice ISTAT Comune", "Latitudine", "Longitudine"]  # List of columns to remove.
    data_cleaned = data.drop(columns=columns_to_drop)
    data_cleaned.fillna('Not found', inplace=True)
    data_cleaned.drop_duplicates(inplace=True)
    return data_cleaned
