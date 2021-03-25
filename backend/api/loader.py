import requests
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import *
from .token import api_token

class Loader():
    def __init__(self):
        self._API_URL = 'https://dekanat.bstu.ru/api/shedule/'

    def _load_teachers(self):
        next_url = self._API_URL + 'employees/'
        while next_url:
            employees_resp = requests.get(
                next_url, headers=api_token.get_headers())
            next_url = employees_resp.json()['next']
            employees = employees_resp.json()['results']
            for employee in employees:
                name = '{} {} {}'.format(employee['surname'],employee['name'],employee['patronymic'])
                try:
                    e = ReviewTarget.objects.get(name=name)
                except ObjectDoesNotExist:
                    ReviewTarget.objects.create(
                        name = name,
                        type = "tch"
                    )
                except MultipleObjectsReturned:
                    print('Обнаружен конфликт! {} и {}'.format(e, employee))

    def _load_subjects(self):
        next_url = self._API_URL + 'dict_subjects/'
        while next_url:
            print(next_url)
            subjects_resp = requests.get(
                next_url, headers=api_token.get_headers())
            next_url = subjects_resp.json()['next']
            subjects = subjects_resp.json()['results']
            for subject in subjects:
                try:
                    s = ReviewTarget.objects.get(subject['name'])
                except ObjectDoesNotExist:
                    ReviewTarget.objects.create(
                        name=subject['name'],
                        type="sbj"
                    )
                except MultipleObjectsReturned:
                    # TODO придумать что нибудь поизящнее
                    print('Обнаружен конфликт! {} и {}'.format(s, subject))

    def _load_groups(self):
        next_url = self._API_URL + 'groups/'
        while next_url:
            print(next_url)
            groups_resp = requests.get(
                next_url, headers=api_token.get_headers())
            next_url = groups_resp.json()['next']
            groups = groups_resp.json()['results']
            for group in groups:
                try:
                    g = Group.objects.get(name=group['name'])
                except ObjectDoesNotExist:
                    Group.objects.create(
                        name=group['name'],
                    )
                except MultipleObjectsReturned:
                    # TODO придумать что нибудь поизящнее
                    print('Обнаружен конфликт! {} и {}'.format(g, group))

    def update_all(self):
        #self._load_teachers()
        self._load_groups()
        self._load_subjects()

loader = Loader()