from uk_covid19 import Cov19API


def fetch_covid_csv():
    england_only = [
        'areaType=nation',
        'areaName=England'
    ]

    columns = {
        "date": "date",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "hospitalCases": "hospitalCases",
        "newPillarOneTestsByPublishDate": "newPillarOneTestsByPublishDate",
        "newPillarTwoTestsByPublishDate": "newPillarTwoTestsByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
    }

    api_request = Cov19API(filters=england_only, structure=columns)
    csv_data = api_request.get_csv()

    return csv_data



if __name__ == '__main__':
    import sys
    output_filename = sys.argv[1]
    with open(output_filename, 'w') as f:
        data = fetch_covid_csv()
        f.write(data)
