from flask import render_template,request,redirect,url_for
from app import app,auth,gf,api


@app.route('/logout')
def logout():
	auth.Adminuser["isAuthenticated"] = False
	return redirect(url_for("login"))


@app.route('/index')
@app.route('/', methods=['GET','POST'])
def login():	

	form = gf.Map(request.form.to_dict());
	user_ = auth.authenticate(form.username,form.password,form)

	if user_ and user_["isAuthenticated"]:
		if user_["in_company"] is None:
			user_ = auth.authenticate(form.username,form.password,form)
		
			return render_template("login.html",title="Base | Login",form=form,user=user_,companies=user_["companies"])
		else:
			if auth.Adminuser["session"] is None: 
				auth.Adminuser["session"] = api.createSession(user_)

			return render_template("index.html",title="Base | Home",year=gf.year(),user=user_)

	return render_template("login.html",title="Base | Login",form=[1],user=user_) 
