from flask import Flask, render_template
from blueprints.user.models import User
from blueprints.post.models import Post
from blueprints.auth.views import bp as bp_auth
from blueprints.post.views import bp as bp_post


app = Flask(__name__)
app.secret_key = 'qwerty123'
app.debug = True


@app.route('/')
def home():
    from blueprints.post.forms import PostForm
    form = PostForm()
    posts = Post.select().order_by(Post.date.desc())
    return render_template('home.html', form=form, posts=posts)


User.create_table()
Post.create_table()


app.register_blueprint(bp_auth)
app.register_blueprint(bp_post)


# home -> all posts from all users
# user blueprint -> all posts from selected user / ...
# auth blueprint -> login / logout / register
