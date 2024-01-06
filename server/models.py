from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import func

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    @validates('name')
    def validate_author_name(self, key, name):
        # Ensure all authors have a name
        if not name:
            raise ValueError("Author must have a name.")
        return name

    @validates('phone_number')
    def validate_author_phone_number(self, key, phone_number):
        # Ensure author phone numbers are exactly ten digits
        if phone_number and len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Author phone number must be exactly ten digits.")
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    @validates('title')
    def validate_post_title(self, key, title):
        # Ensure all posts have a title
        if not title:
            raise ValueError("Post must have a title.")
        return title

    @validates('content')
    def validate_post_content(self, key, content):
        # Ensure post content is at least 250 characters long
        if content and len(content) < 250:
            raise ValueError("Post content must be at least 250 characters long.")
        return content

    @validates('summary')
    def validate_post_summary(self, key, summary):
        # Ensure post summary is a maximum of 250 characters
        if summary and len(summary) > 250:
            raise ValueError("Post summary must be a maximum of 250 characters.")
        return summary

    @validates('category')
    def validate_post_category(self, key, category):
        # Ensure post category is either Fiction or Non-Fiction
        allowed_categories = ['Fiction', 'Non-Fiction']
        if category not in allowed_categories:
            raise ValueError("Post category must be either Fiction or Non-Fiction.")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'
