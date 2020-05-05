from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Board)
admin.site.register(Commit)
admin.site.register(Liked)
admin.site.register(CommitLiked)