import pathlib

import parus.config as config

DUMMY_PARUS_DIR = pathlib.Path('home', '.parus')


def test_default_credentials_file():
    default_creds_file = pathlib.Path.home().joinpath('.parus', 'credentials.json')

    creds_file = config.get_default_credentials_file()

    assert creds_file == default_creds_file


def test_token_file_from():
    creds_file = DUMMY_PARUS_DIR.joinpath('credentials.json')

    token_file = config.token_file_for(creds_file)

    assert token_file == DUMMY_PARUS_DIR.joinpath('google-api-token.json')
