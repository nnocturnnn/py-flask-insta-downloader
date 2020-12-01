from flask import Flask, render_template,request, url_for, redirect , session
import instagram
from redis import Redis
from flask_sqlalchemy import SQLAlchemy

# import rq

app = Flask(__name__)
app.secret_key = 'iknowyoucanseethis'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/')
@app.route('/home')
@app.route('/index')



def home(methods=['GET', 'POST']):
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("index.html")

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        result = request.form
        username=(result['userid'])
    '''
    id=''
    try:
        id=instagram.getID(username)
        if id=='invalid_username':
            return '<h1>Invalid Username</h1><br><h2>Please go back and enter a valid username to continue</p>'
    except Exception as e:
        print(e)
    try:
        user_data=instagram.userDetails(id)
    except Exception as e:
        print(e)
    '''
    profile = instagram.userDetails(username)
    if profile is None:
        return '<h1>Invalid Username</h1><br><h2>Please go back and enter a valid username to continue</p>'

    dp_url = profile.profile_pic_url
    hd_dp_url = profile.profile_pic_url
    username = profile.username
    fullname = profile.full_name
    private_profile = profile.is_private
    is_verified = profile.is_verified
    total_posts = profile.mediacount
    followers = profile.followers
    following = profile.followees
    bio = profile.biography 
    if bio is None:
        bio ='None'
    external_url = profile.external_url
    if external_url is None:
        external_url='None'
    return render_template("display.html",dp_url=dp_url,username=username,fullname=fullname,private_profile=private_profile,is_verified=is_verified,total_posts=total_posts,followers=followers,following=following,bio=bio,external_url=external_url,hd_dp_url=hd_dp_url)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/post', methods=['GET', 'POST'])
def post():
    try:
        if request.method == 'GET':
            return render_template("downloadpost.html")
        else:
            result = request.form
            post_link = (result['postlink'])
            full_name,followers,followees,is_verified,is_private,bio,external_url, owner_username, url, caption, caption_hashtags, caption_mentions, is_video, media_url, likes, comments = instagram.get_media_details(post_link)
            return render_template('post.html',full_name=full_name,followers=followers,followees=followees,is_verified=is_verified,is_private=is_private,bio=bio,external_url=external_url,owner_username=owner_username,url=url,caption=caption,caption_hashtags=caption_hashtags,caption_mentions=caption_mentions,is_video=is_video,comments=comments,likes=likes,media_url=media_url)
    except :
        return "Something went wrong. Is your URL Correct? Make sure the link isn't Private."

if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
