from django.contrib import admin

# Register your models here.
from emphub.models import Department,Position,Project

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Project)
