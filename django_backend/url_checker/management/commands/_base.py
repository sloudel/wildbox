import requests


def check(url: str) -> int | None:
    """
    HTTP GET request url, returns response status code
 
    :param url: url to request
    :return: http response status code
    """
    try:
        return requests.get(url).status_code
    except Exception as exc:
        print(f'check {url=} error: {exc=}')