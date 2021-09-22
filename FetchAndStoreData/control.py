
from . import fetchDataFromAPI, arrangeData


def controller():
    # Call External APi
    data = fetchDataFromAPI.fetchDatafromAPI()

    print(data[1])

    # Extract relevant reviews
    data = arrangeData.arrangeData(data)

    # Connect to Database

    # Store into Database

    # Read from Database
