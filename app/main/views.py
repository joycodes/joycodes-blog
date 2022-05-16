from flask import render_template,request, redirect, url_for,abort
from flask_login import login_required, current_user

from .. import photos,db
from . import main
from .forms import PostForm, CommentForm, UpdateProfile
from ..models import Post, Comment, User, Upvote, Downvote
from ..requests import get_quotes


@main.route('/')
def index():
    quotes = get_quotes()
    print(quotes)
    posts = Post.query.all()
    product = Post.query.filter_by(category='product').all()
    idea = Post.query.filter_by(category='idea').all()
    business = Post.query.filter_by(category='Business').all()
    return render_template('index.html', business=business, product=product, idea=idea, posts=posts, quotes=quotes)


@main.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    posts = Post.query.all()
    likes = Upvote.query.all()
    user = current_user
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        post_obj = Post(post=post, title=title, category=category, user_id=user_id)
        post_obj.save()
        return redirect(url_for('main.posts'))
    
    return render_template('posts_display.html', posts=posts, likes=likes, user=user,form=form)





@main.route('/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    user = User.query.all()
    comments = Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment,
            post_id=post_id,
            user_id=user_id
        )
        new_comment.save()
        new_comments = [new_comment]
        print(new_comments)
        return redirect(url_for('.comment', post_id=post_id))
    return render_template('comment.html', form=form, post=post, comments=comments, user=user)


@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user)


@main.route('/user/<name>/update_profile', methods=['POST', 'GET'])
@login_required
def update_profile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.user', name=user.username))
    return render_template('profile/update_profile.html', form=form)


@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def upvote(id):
    post = Post.query.get(id)
    vote_mpya = Upvote(post=post, upvote=1)
    vote_mpya.save()
    return redirect(url_for('main.posts'))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
    post = Post.query.get(id)
    vm = Downvote(post=post, downvote=1)
    vm.save()
    return redirect(url_for('main.posts'))

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.user',name=name))