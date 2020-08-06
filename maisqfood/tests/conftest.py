import pytest
from maisqfood.app import create_app

@pytest.fixture(scope="module")
# Instance of Main flask app
def app():
    return create_app()