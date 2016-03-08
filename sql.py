# sql.py - Create a SQLite3 table and populate it with data

import sqlite3

with sqlite3.connect("blog_posts.db") as connection:

	# get a cursor object used to execute SQL commands
	c = connection.cursor()

	# delete the table if it doesn't exist
	#c.execute('DROP TABLE posts')

	# create the table
	c.execute('CREATE TABLE posts(title TEXT, description TEXT)')

	# insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Lorem Ispum", "Lorem Ipsum dolor sit amet.")')
	c.execute('INSERT INTO posts VALUES("Ice cream", "I delicious.")')
	c.execute('INSERT INTO posts VALUES("Pizza", "Mmmm pizza")')
	c.execute('INSERT INTO posts VALUES("Hello world", "My very first blog post!.")')

print("Created Database!")