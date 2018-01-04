from app import db

class Access(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User',back_populates="access",foreign_keys=user_id)

	role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
	role = db.relationship("Role")

	company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
	company = db.relationship('Company',back_populates="users",foreign_keys=company_id)

	def __repr__(self):
		return '<Access %s,%s,%s>' % (self.user_id,self.role_id,self.company_id)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), index=True, unique=True)
	fullname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(220), index=True, unique=True)
	created_date = db.Column(db.DateTime)
	image = db.Column(db.String(1024))

	access = db.relationship('Access',back_populates="user")
	companies = db.relationship('Company',back_populates="owner")
	sessions = db.relationship('Session',back_populates="user")
	orders = db.relationship('Order',back_populates="user")

	def __repr__(self):
		return '<User %s,%s,%s,%s,%s>' % (self.username,self.fullname,self.email,self.password,self.created_date)

class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), index=True, unique=True)
	created_date = db.Column(db.DateTime)
	active = db.Column(db.Boolean)
	level = db.Column(db.Integer)

	def __repr__(self):
		return '<Role %s,%s,%s>' % (self.name,self.created_date,self.active)

class Session(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	session_ = db.Column(db.String(32),unique=True)
	created_date = db.Column(db.DateTime)
	active = db.Column(db.Boolean)

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User',back_populates="sessions",foreign_keys=user_id)

	company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
	company = db.relationship('Company',back_populates="sessions")

	def __repr__(self):
		return '<Session %s,%s,%s,%s,%s>' % (self.session_,self.created_date,self.active,self.user_id,self.company_id)

