from django.contrib import admin

from models import *

"""
class MyModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'ctime'
    list_display = ('id', 'utime', 'ctime')

admin.site.register(MyModel, MyModelAdmin)
"""
