from flask import (
	Flask, 
	render_template, 
	g
)

import sqlite3

app = Flask(__name__)
app.database = "blog_posts.db"

def connect_db():
	return sqlite3.connect(app.database)

@app.route('/posts')
def posts():
	g.db = connect_db()
	cur = g.db.execute("select * from posts")
	posts = [dict(title=row[0], description=row[1]) for row in cur.fetcha11()]
	g.db.close()
	return render_template("posts.html", posts=posts)

if __name__ == '__main__':
	app.run(debug=True)