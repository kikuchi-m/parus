import pathlib

CONFIG_DIR_NAME = '.parus'
CREDENTIALS_FILE_NAME = 'credentials.json'
TOKEN_FILE_NAME = 'google-api-token.json'


def get_default_credentials_file():
    return pathlib.Path.home().joinpath(CONFIG_DIR_NAME, CREDENTIALS_FILE_NAME)


def token_file_for(credentials_file):
    return pathlib.Path(credentials_file).parent.joinpath(TOKEN_FILE_NAME)
