from django.contrib import admin
from .models import FriendRequest, Profile
from .models import Post

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ProfileAdmin(UserAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)
admin.site.register(FriendRequest)
