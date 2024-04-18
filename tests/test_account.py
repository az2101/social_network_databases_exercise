import pytest
from lib.account import *

"""
Constructs with a username and email
"""

def test_account_constructs():
    account = Account(1, 'test username', 'test@email.net')
    assert account.id == 1
    assert account.username == 'test username'
    assert account.email == 'test@email.net'

