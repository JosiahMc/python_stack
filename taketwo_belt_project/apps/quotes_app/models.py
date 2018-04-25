from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
import time

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        context = {
            'status': False
        }
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "***First name must be at least 3 characters, JABRONNNI!***"
        if len(postData['last_name']) < 3:
            errors['last_name'] = "***Last name must be at least 3 characters***"
        if User.objects.filter(email=postData['email']).count() > 0:
            errors['email'] = "***This email {} already exist***".format(postData['email'])
        if postData['birthday'] > time.strftime("%Y-%m-%d"):
            errors['bday'] = '***No time travlers please!.***'
        if len(postData['password']) < 8:
            errors['password_length'] = "***Password must be at least 8 characters***"
        context['errors'] = errors
        if len(errors) == 0:
            context['status'] = True
            hash_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            context['newUser'] = self.create(first_name=postData['first_name'],last_name=postData['last_name'], email=postData['email'], password=hash_pw)       
        return context
    def login_validator(self, postData):
        context = {
            'status': False
        }
        errors = {}
        check_user = User.objects.filter(email = postData['email'])
        check_pass = postData['password']
        if not check_user:
            errors['noUser'] = "***Invalid email, register or type less dumbly***"    
        elif not bcrypt.checkpw(check_pass.encode(), check_user[0].password.encode()):
            errors['wrongPW'] = "***Incorrect password THINK HARDER***"
        context['errors'] = errors
        if len(errors) == 0:
            context['status'] = True
            context['user'] = check_user[0]
        return context
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    birthday = models.DateField(auto_now = False, auto_now_add = False, default= '1900-04-25')
    objects = UserManager()
   

class quoteManager(models.Manager):
    def quote_validator(self, id, postData):
        context = {
            'status': False
        }
        errors = {}
        if len(postData['author']) < 3:
            errors['author'] = "Author name must be at least 3 letters long."
        if len(postData['content']) < 10:
            errors['quote'] = "Quote must be at least 10 characters long."
        context['errors'] = errors
        if len(errors) == 0:
            context['new_quote'] = self.create(author=postData['author'], content=postData['content'], posted_by = User.objects.get(id = id)) 
            context['status'] = True
        return context

    def faveQuote(self, id, postData):
        user = User.objects.get(id = id)
        quote = self.get(id = postData['this_quote'])
        quote.faved_by.add(user)
       
    def unfaveQuote(self, id, postData):
        user = User.objects.get(id = id)
        quote = self.get(id = postData['this_quote'])
        quote.faved_by.remove(user)
      

class Quote(models.Model):
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    #a user can post many quotes but a quote can only be posted by one user
    posted_by = models.ForeignKey(User, related_name="quotes")
    #a user can have many faves and a quote can be favorited by many users
    faved_by = models.ManyToManyField(User, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = quoteManager()
   
