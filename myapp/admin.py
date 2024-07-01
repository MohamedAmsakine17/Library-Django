# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myapp.models import Profile
from .models import Book
from django.utils.safestring import mark_safe  # Import mark_safe


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available_copies', 'display_cover_image')
    search_fields = ('title', 'author')  # Enable searching by title or author
    readonly_fields = ('display_cover_image',)  # Display the current image

    def display_cover_image(self, obj):
        if obj.cover_image:
            return mark_safe(f'<img src="{obj.cover_image.url}" style="max-height:200px;"/>')
        else:
            return 'No image found'
    
    display_cover_image.short_description = 'Cover Image Preview'