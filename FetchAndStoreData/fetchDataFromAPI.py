import requests


def fetchDatafromAPI():
    api_url = api_url = "https://api.rainforestapi.com/request?api_key=AB0A572943E2417784001C2E1F4BBC10&type=product&amazon_domain=amazon.com&asin=B073JYC4XM"
    response = requests.get(api_url)
    return response.json()
