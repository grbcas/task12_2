import pytest

from utils.dicts import get_val


TEST_DICT = {"vcs": "mercurial", "any": ""}


@pytest.fixture
def test_data():
	return TEST_DICT


def test_get_val(test_data):
	assert get_val(test_data, 'vsc', '') == ''
	assert get_val(test_data, 'nokey') == 'git'
	assert get_val(test_data, '', 'bazaar') == 'bazaar'
	assert get_val(test_data, '') == 'git'
