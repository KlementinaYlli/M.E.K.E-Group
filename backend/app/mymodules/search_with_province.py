"""
Schools by province module.

Contains search by province feature.
"""


import json


def schools_by_province(province: str, df):
    """
    Find the schools in the specified province.

    Args:
        province_name (str): province name
        df (Dataframe): dataframe contaning data

    Returns:
        dict: dictionary that contains the specified result as json
    """

    # Run the query and format the output. I do the transposition of the
    # table, so as to have a convenient output to use.
    result = df[df['Denominazione Provincia'].str.lower() == province.lower()].transpose()

    # Return a json with the formatted data.
    return {'result': json.loads(result.to_json())}
