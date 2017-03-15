"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for,flash
from form import CreateProfileForm, LoginForm
from datetime import datetime
from model import Profile
import os
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile',methods=['GET','POST'])
def register():
    form = CreateProfileForm(request.form)

    print "###NAME{}".format(form.firstname.data)
    if request.method == 'POST':#and form.validate():
        print "###############################################################"
        profile = Profile(form.firstname.data, form.lastname.data, form.username.data, form.gender.data, form.age.data, form.bio.data, form.password.data, datetime.utcnow())
        print "LETS see{}".format(profile)
        print "###############################################################"
        print form.firstname.data
        db.session.add(profile)
        db.session.commit()
        file = request.files['file']
        filename = file.filename#form.username.data#file.filename
        file.save(os.path.join("app/static/profilepics", filename))
        flash('Thank you for registering')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/profiles',methods=['GET'])
def getprofiles():
    return

@app.route('/profile/<userid>',methods=['GET'])
def indProfile(userid):
    profile="fo"
    return render_template('profile.html',profile=profile)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(u'Successfully logged in as %s' % form.user.username)
        session['user_id'] = form.user.id
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
