import json
import os
import time

import joblib
import requests
from dotenv import load_dotenv

# from time import sleep


load_dotenv()


class AuthUser:
    def __init__(self) -> None:
        self.file_cache = os.getenv('FILE_CACHE')

    def check_time_file_cache(self, file_cache):

        if os.path.exists(file_cache):
            # Verifique a data de modificação do arquivo de cache
            time_since_update = time.time() - os.path.getmtime(file_cache)
            print(time_since_update)
            # Se o cache tiver mais de 1 dia, exclua-o
            if time_since_update > 86400:  # 86400 segundos em 1 dia
                os.remove(file_cache)

    # Create ou Read token login
    def CR_token_login(self, username, password):
        file_cache = str(self.file_cache)
        self.check_time_file_cache(file_cache)
        try:
            auths_tokens = joblib.load(self.file_cache)
        except FileNotFoundError:
            url = f'{os.getenv("URL_SITE")}accounts/api/token/'
            body_request = {
                "username": username,
                "password": password
            }
            body_request = json.dumps(body_request)
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.request(
                "POST", url=url, headers=headers, data=body_request)
            if response.status_code == 200:
                resp = json.loads(response.text)
                auths_tokens = {
                    'refresh': resp['refresh'],
                    'access': resp['access']
                }
                joblib.dump(auths_tokens, self.file_cache)
            else:
                return False
        return auths_tokens

    def get_infos_user(self):
        try:
            auths_tokens = joblib.load(self.file_cache)
            access = auths_tokens.get('access')
            url = f'{os.getenv("URL_SITE")}accounts/api/v2/'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access}'
            }
            response = requests.request(
                "GET", url=url, headers=headers)
            resp = json.loads(response.text)
            if 'detail' in resp:
                raise Exception('Token Invalido/Expirado')
            return resp.get("results", None)
        except FileNotFoundError:
            return False

    def refresh_token_user(self, token_refresh):
        url = f'{os.getenv("URL_SITE")}accounts/api/token/refresh/'
        body_request = {
            "refresh": token_refresh,

        }
        body_request = json.dumps(body_request)
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.request(
            "POST", url=url, headers=headers, data=body_request)
        if response.status_code == 200:
            resp = json.loads(response.text)
            auths_tokens = {
                'refresh': token_refresh,
                'access': resp['access']
            }
            joblib.dump(auths_tokens, self.file_cache)
            return True
        return False


def format_phone_url(phone):
    new_phone = f'{phone}'.replace('(', '').replace(
        ')', '').replace('-', '').replace(' ', '')
    if '55' not in new_phone:
        new_phone = f'55{new_phone}'
    return new_phone


def verifica_acesso_internet():
    try:
        response = requests.get("https://www.google.com")
        response.raise_for_status()
        print("Você tem acesso à internet!")
        return True
    except requests.exceptions.RequestException:
        print("Não foi possível acessar a internet.")
        return False


class GrupoOportunidade:
    def __init__(self) -> None:
        self.url = os.getenv('URL_SITE')
        self.auth = AuthUser()
        try:
            self.file_cache = os.getenv('FILE_CACHE')
        except FileNotFoundError:
            self.file_cache = None
        self.auths_tokens = joblib.load(self.file_cache)

    def get_tigger_file(self):
        if self.file_cache:
            access = self.auths_tokens.get('access')
            refresh = self.auths_tokens.get('refresh')
            url = f'{os.getenv("URL_SITE")}accounts/api/FileCSV/'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access}'
            }
            try:
                response = requests.request(
                    "GET", url=url, headers=headers)
                resp = json.loads(response.text)
                if 'code' in resp:
                    if resp['code'] == 'token_not_valid':
                        self.auth.refresh_token_user(refresh)
                        return self.get_tigger_file()
                return resp['results']
            except requests.exceptions.ConnectionError:
                return {'error': 'Erro na conexão com a API'}
        return {'error': 'Necessário Login!'}

    def update_group_opportunities(self, grupo):
        if self.file_cache:
            access = self.auths_tokens.get('access')
            url = f'{os.getenv("URL_SITE")}accounts/api/marcar_grupo/{grupo}/'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access}'
            }
            body = {
                'disparado': True
            }
            try:
                response = requests.request(
                    "PATCH", url=url, headers=headers, data=json.dumps(body))
                resp = json.loads(response.text)
                return resp
            except requests.exceptions.ConnectionError:
                return {'error': 'Erro na conexão com a API'}
        return {'error': 'Necessário Login!'}


if __name__ == '__main__':
    conn = verifica_acesso_internet()
    print(conn)
    grupo = GrupoOportunidade()
    grupo_id = grupo.get_tigger_file()
    grupo_id = grupo_id
    grupo_id = grupo_id[0]['participantes']
    print(grupo_id)

    # auth = AuthUser()
    # tokens = auth.CR_token_login('admin', 'j040v1t0r')
    # # access_token = tokens.get('access', None)
    # # print(access_token)
    # try:
    #     infos_user = auth.get_infos_user()
    # except Exception:
    #     file_cache = os.getenv('FILE_CACHE')
    #     auths_tokens = joblib.load(file_cache)
    #     refresh = auths_tokens['refresh']
    #     refresh_token = auth.refresh_token_user(refresh)
    #     print(refresh_token)
    #     if refresh_token:
    #         infos_user = auth.get_infos_user()
    #     else:
    #         infos_user = None
    # print(infos_user)
