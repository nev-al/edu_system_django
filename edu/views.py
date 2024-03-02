from django.http import JsonResponse
from .models import *
from statistics import mean


def available_products(request):
    _json = dict()
    for i in Product.objects.all():
        _json[f'{i.id}'] = {
            'Product': i.name,
            'Author': i.creator,
            'Launch': str(i.start_date).replace('T', ' '),
            'Price': f'${i.price}',
            'Lessons': i.lesson_set.count()
        }
    return JsonResponse(_json)


def lessons(request, uid):
    _json = {}
    u = User.objects.get(uid=uid)
    for i in Product.objects.all():
        if u in i.user_set.all():
            _json[f'{i.id}'] = {
                'Product': i.name,
                'Lessons': list(i.lesson_set.values_list('name', flat=True))
            }
        if not _json:
            _json['Lessons available']: 0
    return JsonResponse(_json)


def statistics(request):
    _json = {}
    for i in Product.objects.all():
        _json[f'{i.id}'] = {
            'Product': i.name,
            'Paid users': i.user_set.count(),
            'Students Qty': sum([j.size() for j in i.group_set.all()]),
            'Groups Qty': i.group_set.count(),
            'Group fill percentage':
                f'{mean([j.size() / i.max_users_per_group for j in i.group_set.all()]) * 100:.1f}%',
            'Paid users percentage': f'{i.user_set.count() / User.objects.count() * 100:.1f}%'
        }
    return JsonResponse(_json)
