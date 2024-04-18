from lib.database_connection import DatabaseConnection
from lib.account_repository import AccountRepository
from lib.post_repository import PostRepository

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/social_network.sql")

account_repository = AccountRepository(connection)
accounts = account_repository.all()

for account in accounts:
    print (account)

post_repository = PostRepository(connection)
posts = post_repository.all()

for post in posts:
    print (post)

