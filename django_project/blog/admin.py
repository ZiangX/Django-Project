from django.contrib import admin
from .models import Post #Since they are under the same directory

#Note: regirster the Post model to admin site
admin.site.register(Post)