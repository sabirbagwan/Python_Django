from django.contrib import admin
from .models import Post
from .models import Contact

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','featured', 'add_date')
    search_fields = ('title',)
    # list_filter = ('cat',)
    ordering = ('-add_date',)

admin.site.register(Post, PostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'message')
    search_fields = ('name','email')
    ordering = ('email',)

admin.site.register(Contact, ContactAdmin)