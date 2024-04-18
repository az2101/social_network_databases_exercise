import pytest
from lib.post import *
from lib.post_repository import *

"""
#all
get a list of all post objects reflecting seed
"""

def test_get_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()
    assert posts == [
        Post(1,'My Title 1', 'My Content 1', 0, 1),
        Post(2,'My Title 2', 'My Content 2', 0, 2)
    ]


def test_find_singe_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(1)
    assert post == Post(1,'My Title 1', 'My Content 1', 0, 1)


def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = Post(None, 'My Title 3', 'My Contents 3', 10, 1)
    repository.create(post)

    posts = repository.all()
    assert posts == [
        Post(1,'My Title 1', 'My Content 1', 0, 1),
        Post(2,'My Title 2', 'My Content 2', 0, 2),
        Post(3, 'My Title 3', 'My Contents 3', 10, 1)
    ]


def test_delete_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Post(1,'My Title 1', 'My Content 1', 0, 1)
    ]
