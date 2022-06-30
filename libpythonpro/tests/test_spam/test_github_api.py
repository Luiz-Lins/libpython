from unittest.mock import Mock

import pytest
import requests

from libpythonpro import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Luiz-Lins')
    assert 'https://avatars.githubusercontent.com/u/104336322?v=4' == url

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/104336322?v=4'
    resp_mock.json.return_value = {
        'login': 'Luiz-Lins', 'id': 104336322,
        'avatar_url': url,
    }
    get_original = github_api.request.get
    github_api.request.get = Mock(return_value=resp_mock)
    yield url
    github_api.request.get = get_original


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url