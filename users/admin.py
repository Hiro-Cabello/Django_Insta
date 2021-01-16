from django.contrib import admin

# Register your models here.
from users.models import Profile
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone_number','website','picture')
    search_fields=(
        'user__email',
        'user__username',
        'user_first_name',
        'user__last_name',
        'phone_number'
    )
    #Para ingresar los filtros
    list_filter=(
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )