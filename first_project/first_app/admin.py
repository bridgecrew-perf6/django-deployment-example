from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage
from .models import UserProfileInfo, User


# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)


# Register your models here.
admin.site.register(UserProfileInfo)
