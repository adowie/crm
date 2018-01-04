from app import app,db,models,gf
from flask import jsonify,request
from sqlalchemy import *
import sqlalchemy.exc 
import simplejson as json

def createSession(auth_user):
	now = gf.now()
	user = gf.Map(auth_user)
	
	session_ = gf.randomString(16)
	
	user_id = user.id

	session_exist,old_session = sessionExist(user,session_)

	if not session_exist:
		session = models.Session(session_=str(session_),created_date=now,active=1,company_id=user.in_company,user_id=user.id)   
		error = ""

		db_sess = db.session #open database session
		try:
			db_sess.add(session) #add prepared statment to opened session
			db_sess.commit() #commit changes
		except sqlalchemy.exc.SQLAlchemyError, e:
			db_sess.rollback()
			db_sess.flush() # for resetting non-commited .add()
			error = { "error":e,"session":session_}

		if error:
			result = error #[data] #prepare visual data
		else:
			new_session = models.Session.query.filter_by(id=session.id).first()
			result = new_session.session_ #prepare visual data
	else:
		result = old_session.session_ #prepare visual data

	return result

def sessionExist(user,id_):
	session = models.Session.query.filter_by(id=id_).first()
	
	if session is not None:
		return True,session
	else:
		istf,session = getUserActiveSession(user)
		return istf,session

def getUserActiveSession(user):
	user_ = models.User.query.filter_by(id=user.id).first()
	
	if len(user_.sessions) > 0:
		for session in user_.sessions:
			if str(gf.datetimeToDate(session.created_date)) == str(gf.today()) and int(session.company_id) == int(user.in_company):
				# print(session)
				return True,session
			

	return False,None

