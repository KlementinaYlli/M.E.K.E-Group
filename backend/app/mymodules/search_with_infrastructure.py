"""
Search with infrastructure module.

Contains search with infrastructure feature.
"""

__possible_infrastructures = ["Spazi Didattici", "Auditorium Aula Magna", "Mensa", "Palestra Piscina", "Spazi Amministrativi"]


def search_with_infrastructure(province_name, infrastructure_name: str, df):
    """
    Find the schools with specified infrastructure.

    Args:
        province_name (str): province name
        infrastructure_name (str): infrastructure name
        data (DataFrame): the DataFrame containing the data

    Returns:
        Dataframe | None: information on the school with the selected infrastructure.
        If there is no data available then returns None.
    """

    # Check if the province exists in the dataset
    if province_name.upper() not in df['Denominazione Provincia'].str.upper().unique():
        return None

    # Controlla se la lista delle infrastrutture è vuota
    if infrastructure_name not in __possible_infrastructures:
        return None

    # Check if the infrastructure list is empty
    with_province = df[df['Denominazione Provincia'].str.upper() == province_name.upper()]

    with_infrastructure = with_province[with_province[infrastructure_name] > 0]

    return with_infrastructure
