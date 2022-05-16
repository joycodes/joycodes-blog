from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class  Quotes:
    '''
    Qoutes class to define quotes Objects
    '''
    
    def __init__(self,author,id,quote,permalink):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink
    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,
        primary_key=True)
    username= db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    password_sec = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.password_sec = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_sec,
            password)
    
    def __repr__(self):
        return f'User: {self.username}'
    
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    user_id = db.Column(db.String() )
    post = db.Column(db.String())
    comment = db.relationship('Comment', backref='post', lazy='dynamic')
    category = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    up_vote = db.relationship('Upvote', backref='post', lazy='dynamic')
    down_vote = db.relationship('Downvote', backref='post', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post Title: {self.title}"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    comment = db.Column(db.Text())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'


class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls, id):
        upvote_post = Upvote(user=current_user, post_id=id)
        upvote_post.save()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(post_id=id).all()
        return upvote

    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls, id):
        downvote_post = Downvote(user=current_user, post_id=id)
        downvote_post.save()

    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(post_id=id).all()
        return downvote

    @classmethod
    def all_downvotes(cls):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'
    