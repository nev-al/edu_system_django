from django.contrib import admin
from .models import User, Product, Group, Lesson


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Group)
admin.site.register(Lesson)