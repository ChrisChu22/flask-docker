import pytest
import requests

from pytest_bdd import scenarios, when, then

ANIME_API = 'https://api.jikan.moe/v3'

scenarios('anime.feature', example_converters=dict(number=str, title=str))


@pytest.fixture
@when('the Anime API is queried with "<number>"')
def anime_response(number):
    params = {'format': 'json'}
    response = requests.get(ANIME_API + '/anime/' + number, params=params)
    return response


@then('the response shows title of "<title>"')
def anime_response_title(anime_response, title):
    assert title == anime_response.json()['title']


@then('the response status code is 200')
def anime_response_code(anime_response):
    assert anime_response.status_code == 200
