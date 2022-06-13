from django.contrib import admin
from home.models import Contact
from home.models import Contact_1
from .models import *

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Profile)

admin.site.register(Contact)
admin.site.register(Contact_1)