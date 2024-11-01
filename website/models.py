from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__ = 'user'

    user_id = db.Column(db.String(10), primary_key=True, nullable=False)
    username = db.Column(db.String(50), nullable=True)
    doc = db.Column(db.Date, nullable=True)
    accstatus = db.Column(db.Enum('ACTIVE', 'BANNED'), default='ACTIVE')
    email_id = db.Column(db.String(50), nullable=True, unique = True)
    first_name = db.Column(db.String(50), nullable=True)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True) 
    password = db.Column(db.String(50), nullable = True) 

class Channel(db.Model, UserMixin):
    __tablename__ = 'channel'

    channel_id = db.Column(db.String(10), primary_key=True, nullable=False)
    username = db.Column(db.String(50), nullable=True)
    email_id = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=True)
    date_of_creation = db.Column(db.Date, nullable=True)
    acc_status = db.Column(db.Enum('ACTIVE', 'BANNED'), default='ACTIVE')
    user_id = db.Column(db.String(9), db.ForeignKey('user.user_id'), nullable=True) 


class Video(db.Model, UserMixin):
    __tablename__ = 'video'
    
    video_id = db.Column(db.String(10), primary_key=True, nullable=False)
    video_title = db.Column(db.String(50), nullable=False)
    posted_date = db.Column(db.Date, nullable=True, default=None)
    views = db.Column(db.BigInteger, nullable=True, default=None)
    comments = db.Column(db.BigInteger, nullable=True, default=None)
    likes = db.Column(db.BigInteger, nullable=True, default=None)
    dislikes = db.Column(db.BigInteger, nullable=True, default=None)
    channel_id = db.Column(db.String(10), db.ForeignKey('channel.channel_id'), nullable=True)
    ad_id = db.Column(db.String(10), db.ForeignKey('sponser.ad_id'), nullable=True) 

class Sponser(db.Model, UserMixin):
    __tablename__ = 'sponser'
    
    ad_id = db.Column(db.String(10), primary_key=True, nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(50), nullable=True, default=None)
    phone_no = db.Column(db.String(10), nullable=True, default=None)
    email_id = db.Column(db.String(50), nullable=True, default=None)
    company_website = db.Column(db.String(30), nullable=True, default=None)
