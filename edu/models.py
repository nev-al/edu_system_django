from django.db import models
import uuid
import time


class Product(models.Model):
    name = models.CharField(max_length=128)
    creator = models.CharField(max_length=128)
    start_date = models.DateTimeField()
    max_groups = models.IntegerField(default=5)
    min_users_per_group = models.IntegerField(default=3)
    max_users_per_group = models.IntegerField(default=12)
    price = models.FloatField()

    def clean_groups(self):
        for i in self.group_set.all():
            i.users.clear()

    def united_users_from_all_group_by_product(self):
        lst = []
        for i in self.group_set.all():
            lst.append(i.users.all())
        return models.QuerySet.union(*lst) if len(lst) > 0 else models.QuerySet()

    def paid_users_without_group(self):
        return self.user_set.all().difference(self.united_users_from_all_group_by_product())

    def user_rearrangement(self):
        if time.time() < time.mktime(self.start_date.timetuple()) and len(self.paid_users_without_group()) > 0:
            groups = list(self.group_set.all())
            for i in groups:
                i.users.clear()
            users_to_distribute = list(self.paid_users_without_group())
            index = 0
            while len(users_to_distribute) > 0 and len(groups) > 0:
                index = 0 if index >= len(groups) else index
                if groups[index].size() < self.max_users_per_group:
                    groups[index].users.add(users_to_distribute.pop())
                    index += 1
                else:
                    groups.remove(groups[index])

    def correct_group_qty(self):
        self.user_rearrangement()
        for i in self.group_set.all():
            if self.group_set.count() > 1 and i.size() < self.min_users_per_group:
                i.delete()
                self.user_rearrangement()
                self.correct_group_qty()
        self.user_rearrangement()

    def __str__(self):
        return f'course {self.name} ({self.id})'


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    name = models.CharField(max_length=128)
    uid = models.UUIDField(default=uuid.uuid4, editable=True)
    purchased_products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.name}, id: {self.id}'


class Group(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def size(self):
        return self.users.count()

    def __str__(self):
        return f'group {self.name} of product {self.product}'
