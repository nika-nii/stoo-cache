from django.contrib import admin
from .models import *

admin.site.register(Group)
admin.site.register(Review)
admin.site.register(ReviewTarget)