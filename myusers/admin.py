from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from myusers.forms import UserChangeForm
from myusers.forms import UserCreationForm
from myusers.models import MyUser


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'username',            
        'date_of_birth',
        'email',
        'firstname',
        'is_admin',
        'is_superuser',
        'lastname',
        'middlename',
        'is_company',
        #'company',
    ]

    list_filter = ('is_admin',)

    fieldsets = (
                (None, {'fields': ('username', 'password')}),
                ('Personal info', {
                 'fields': (
                     'email',       
                     'date_of_birth',
                     'firstname',
                     'lastname',
                     'middlename',
                     'is_company',
                     'company',
                     'is_active',
                 )}),
                ('Permissions', {'fields': ('is_admin',)}),
                ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',       
                'date_of_birth',
                'email',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

# Регистрация нашей модели
admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)