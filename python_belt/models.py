from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    # validate user function
    def register_validate(self, post):
            result = {'errors':[]}
            if len(post['name']) < 4:
                result['errors'].append('Please enter your Full Name.')
                return result
            elif not re.search(r'\w+\@\w+\.\w+', post.get('email')):
                result['errors'].append('Please enter a valid email')
                return result
            elif len(post['password']) < 8:
                result['errors'].append('Password must be 8 or more characters')
                return result
            elif post['confirm_password'] != post['password']:
                result['errors'].append('Passwords must match')

                return result
            else:
                return
    # Create user function
    def create_user(self, post):
        user = User.objects.create(name=post.get('name'), email=post.get('email'), password=post.get('password'), date_of_birth=post.get('dob'))
        return user
    # login validate function
    def login_validate(self, post):
        user = User.objects.filter(email=post.get('email')).first()
        if user and post['password'] == user.password:
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'message': 'Please enter valid credintials'}
    # Login user function
    def login(self, request, user):
        if ('user_id' not in request.session):
            request.session['user_id'] = user.id

class QuoteManager(models.Manager):
    # validation
    def quote_validation(self, post):
        result = {'errors':[]}
        if len(post['author']) < 3:
            result['errors'].append('Please enter a Full Name.')
            return result
        elif len(post['quote']) < 1:
            result['errors'].append('Please enter a quote longer then 10 words.')
            return result
        else:
            return

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=1000)
    date_of_birth = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quotes(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    user = models.ForeignKey(User, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

class Favorite(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
