from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register (Trialworkshop)
admin.site.register (Payworkshop)
admin.site.register (Feedbackform)

