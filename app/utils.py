import requests
from .config import Config
def get_access_token(code):
    url = 'https://github.com/login/oauth/access_token'
    payload = {
        'client_id': Config.CLIENT_ID,
        'client_secret': Config.CLIENT_SECRET,
        'code': code,
        'redirect_uri': Config.REDIRECT_URI
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()['access_token']

def get_user_login_id(access_token):
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()['id']

def invite_user_to_organization(user_login_id, access_token):
    url = f'https://api.github.com/orgs/{Config.ORGANIZATION_NAME}/invitations'
    payload = {'invitee_id': user_login_id}
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response