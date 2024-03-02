from edu.models import User, Product, Group, Lesson
from django.db.models.query import QuerySet
import random
from datetime import datetime
import time
from statistics import mean
from faker import Faker


# for product in User.objects.all():
#     product.delete()
#
# for product in Group.objects.all():
#     product.delete()

# fake = Faker()
# for i in range(100):
#     u = User(name=fake.name())
#     u.save()
# all_users = User.objects.all()
# for i in Product.objects.all():
#     i.user_set.add(*random.choices(all_users, k=int(len(all_users)*0.8)))
#
# for product in Product.objects.all():
#     for i in range(1, product.max_groups + 1):
#         g = Group(name=f'{product.name}_{i}', product_id=product.id)
#         g.save()

# for i in Product.objects.all():
#     i.correct_group_qty()



