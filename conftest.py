import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture(scope="session")
def app(request):
  fixture = Application()
  request.addfinalizer(fixture.destroy)
  return fixture
