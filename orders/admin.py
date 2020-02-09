from django.contrib import admin
from .models import *
from account.models import *

admin.site.register(WorkStations)
admin.site.register(orders)
admin.site.register(OrderAttachments)
admin.site.register(ProfileDetail)
admin.site.register(UserProject)
admin.site.register(Comment)
admin.site.register(Notifications)