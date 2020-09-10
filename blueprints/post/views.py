from flask import Blueprint, flash, session, url_for, redirect
from .models import Post
from .forms import PostForm


bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/', methods=['POST'])
def make_post():
    form = PostForm()

    if form.is_submitted():
        Post.create(
            user_id=session.get('user_id'),
            text=form.text.data
        )
        flash('Post created successfully', 'success')
        return redirect(url_for('home'))

    flash('Something is wrong with post...', 'danger')
    return redirect(url_for('home'))
