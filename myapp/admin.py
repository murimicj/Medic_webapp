from django.contrib import admin

from myapp.models import Student, Product, Patients, Appointment,Member

# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Patients)
admin.site.register(Appointment)
admin.site.register(Member)


