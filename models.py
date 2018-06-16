from run import db

class Todo(db.Model):
	__table__name = 'user_table'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(80))
	def __init__(self, content):
		self.content= content
	def __repr__(self):
		return '<Todo %r>' % self.content