from app import db,models

Adminuser = {"isAuthenticated":False}#{"username":"adowie","fullName":"Alex Dowie","isAuthenticated":False,"password":"xxxx51234","company":None}
user = {}

def authenticate(name,pass_,company):
	global Adminuser 
	global user

	if name and pass_:
		user = models.User
		auth_user = user.query.filter_by(email=name,password=pass_).first()

		if auth_user is not None:
			if "company" in company:
				if checkUserAccess(auth_user,company.company):
					Adminuser =  {'email':auth_user.email, 'username':auth_user.username,'fullname':auth_user.fullname,"companies":auth_user.companies,"isAuthenticated":True,"in_company":company.company,"company":company.name,"password":pass_,"id":auth_user.id,"session":None}
				else:
					Adminuser = {'email':None,"isAuthenticated":True ,"error":"Access Denied!... %s refused your credentials. Please contact admin for assistance." % company.name,"password":"xxxx","in_company":None,"company":None,"companies":auth_user.companies,"id":auth_user.id,"session":None}	
					
			else:
				Adminuser =  {'email':auth_user.email,'username':auth_user.username,'fullname':auth_user.fullname,"companies":auth_user.companies,"isAuthenticated":True,"in_company":None,"company":None,"password":pass_,"id":auth_user.id,"session":None}

		else:
			Adminuser = {'email':"","isAuthenticated":False ,"error":"Oops!. Email or Password is invalid.","password":"xxxx","in_company":company,"id":None,"session":None}

		return Adminuser

def checkUserAccess(user,company):
	
	if len(user.access) > 0:
		for auth in user.access:
			if int(auth.company_id) == int(company):
				return True
			else:
				return False
	else:
		return False

def getAccess():
	accesses = models.Access.query.all()
	auths = []
	for access in accesses:
		auths.append(access)

	return auths