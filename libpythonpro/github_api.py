import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuário no github
    :param usuario:str com o nome de usuário no github
    :return:str com o link do avatar
    """
    url: str = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


def request():
    return None