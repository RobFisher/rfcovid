import uk_covid19


def fetch_covid_csv():
    england_only = [
        'areaType=nation',
        'areaName=England'
    ]

    columns = {
        "date": "date",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "hospitalCases": "hospitalCases",
        "covidOccupiedMVBeds": "covidOccupiedMVBeds",
        "newPillarOneTestsByPublishDate": "newPillarOneTestsByPublishDate",
        "newPillarTwoTestsByPublishDate": "newPillarTwoTestsByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
    }

    api_request = uk_covid19.Cov19API(filters=england_only, structure=columns)
    csv_data = api_request.get_csv()

    return csv_data



if __name__ == '__main__':
    import sys
    output_filename = sys.argv[1]
    with open(output_filename, 'w') as f:
        try:
            data = fetch_covid_csv()
        except uk_covid19.exceptions.FailedRequestError:
            print('Failed request.')
            sys.exit(1)
        f.write(data)
