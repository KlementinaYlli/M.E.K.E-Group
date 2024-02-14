"""
Listing module.

Contains functions to list different fields of a csv.
"""


def list_provinces(df):
    """
    List all available provinces.

    Args:
        df (DataFrame): the DataFrame containing data

    Returns:
        list: list containing all available provinces
    """

    unique = df.get('Denominazione Provincia').unique()
    return [x for x in unique if x]


def list_cities(df):
    """
    List all available cities.

    Args:
        df (DataFrame): the DataFrame containing data

    Returns:
        list: list containing all available cities
    """

    unique = df.get('Denominazione Comune').unique()
    return [x for x in unique if x]


def list_school_types(df):
    """
    List all available school types.

    Args:
        df (DataFrame): the DataFrame containing data

    Returns:
        list: list containing all available school types
    """

    unique = df.get('Tipologia Scuola').unique()
    return [x for x in unique if x]
