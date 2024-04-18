import pytest
from lib.account import *
from lib.account_repository import *

"""
When we call AccountRepository #all
We get a list of Account objects reflecting the seed data
"""

def test_get_all_accounts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    accounts = repository.all()
    assert accounts == [
        Account(1, 'andrew', 'andrew@andrew.net'),
        Account(2, 'zarei', 'zarei@zarei.net')
    ]

"""
When we call AccountRepository #find
We get a single Account object reflecting the seed data
"""

def test_find_single_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    account = repository.find(1)
    assert account == Account(1, 'andrew', 'andrew@andrew.net')

"""
#create
Creates an Account object
"""

def test_create_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    account = Account(None, 'AddedUser', 'AddedEmail')
    repository.create(account)

    accounts = repository.all()
    assert accounts == [
        Account(1, 'andrew', 'andrew@andrew.net'),
        Account(2, 'zarei', 'zarei@zarei.net'),
        Account(3, 'AddedUser', 'AddedEmail')
    ]

"""
#delete
Delectes Account object
"""

def test_delete_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    repository.delete(2)
    accounts = repository.all()
    assert accounts == [
        Account(1, 'andrew', 'andrew@andrew.net')
    ]
