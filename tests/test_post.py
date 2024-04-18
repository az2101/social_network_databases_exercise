import pytest
from lib.post import *

"""
Constructs with title, contents, views, account_id
"""

def test_post_constructs():
    post = Post(1, 'test title', 'test contents', 0, 1)
    assert post.id == 1
    assert post.title == 'test title'
    assert post.contents == 'test contents'
    assert post.views == 0
    assert post.account_id == 1

    