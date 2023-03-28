from django.contrib import admin
from .models import Room
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


# admin.site.register(
#     Room,
#     list_display=["id", "title", "staff_only"],
#     list_display_links=["id", "title"],
# )

admin.site.register(Room)