from edu.models import User, Product, Group, Lesson
from django.db.models.query import QuerySet
import random
from datetime import datetime
import time
from statistics import mean
from faker import Faker


def delete_all_users():
    for product in User.objects.all():
        product.delete()


def delete_all_groups():
    for product in Group.objects.all():
        product.delete()


def generate_users(qty=100, paid_coeff_of_them=0.8):
    fake = Faker()
    for i in range(qty):
        u = User(name=fake.name())
        u.save()
    all_users = User.objects.all()
    for i in Product.objects.all():
        i.user_set.add(*random.choices(all_users, k=int(len(all_users) * paid_coeff_of_them)))


def generate_groups():
    for product in Product.objects.all():
        for i in range(1, product.max_groups + 1):
            g = Group(name=f'{product.name}_{i}', product_id=product.id)
            g.save()


def correct_all_groups_qty():
    for i in Product.objects.all():
        i.correct_group_qty()


if __name__ == '__main__':
    # delete_all_users()
    # delete_all_groups()
    # generate_users()
    # generate_groups()
    correct_all_groups_qty()

