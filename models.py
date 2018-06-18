from run import db
class User(db.Model):
	__tablename__ = 'user_table'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),nullable=False)
	birthday = db.Column(db.String(10))
	phone = db.Column(db.String(10), unique=True, nullable=False)
	email = db.Column(db.String(255), nullable=False, unique=True) 

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(80),unique=True)
# 	email = db.Column(db.String(120),unique=True)

# 	def __init__(self, username, email):
# 		self.username=username
# 		self.email=email

# 	def __repr__(self):
# 		return '<User %r>'% self.username