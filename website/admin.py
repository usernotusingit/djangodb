from django.contrib import admin
from .models import Member
from .models import Venue
from .models import MyClubUser
from .models import Event

admin.site.register(Member)
admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)

# Register your models here.
