from django.contrib import admin

from models import Thread, Post

class PostInline(admin.StackedInline):
    model = Post
    extra = 1

class ThreadAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject','creator','site','stuck']}),
        ('Last Post Information', {'fields':['last_post_by','last_post']}),
    ]


admin.site.register(Thread,ThreadAdmin)
admin.site.register(Post)

