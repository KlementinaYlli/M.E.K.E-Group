"""
Best school in town feature.

Contains best school in town feature.
"""


def best_school_in_town(city: str, school_level: str, df):
    """
    Find the school with the most services in a city and level
    of specified school.

    Args:
        data (DataFrame): the DataFrame containing the school data
        city (str): the city for which to find the school
        school_level (str): school level (es. 'primaria', 'secondaria primo grado')

    Returns:
        Dataframe | None: information on the school with the greatest number of services
        If there is no data available then returns None.
    """

    filtered_data = df[(df['Denominazione Comune'].str.lower() == city.lower()) &
                       (df['Tipologia Scuola'].str.lower() == school_level.lower())]

    if filtered_data.empty:
        return None

    # Calculates the number of services for each school.
    filtered_data.loc[:, ['Service Count']] = filtered_data[['Spazi Didattici', 'Auditorium Aula Magna', 'Mensa', 'Palestra Piscina', 'Spazi Amministrativi']].sum(axis=1)

    # Sorts by number of services.
    filtered_data = filtered_data.sort_values(by='Service Count', ascending=False)

    best_schools = filtered_data[filtered_data['Service Count'] == filtered_data.iloc[0]['Service Count']]

    return best_schools
