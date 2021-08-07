from django.contrib import admin
from .models import StudentApplication, StaffRegistration, StudentRegistration, Department

admin.site.register(Department)
admin.site.register(StudentApplication)
admin.site.register(StudentRegistration)
admin.site.register(StaffRegistration)
