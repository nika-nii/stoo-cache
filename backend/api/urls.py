from django.urls import path
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from .loader import loader

from .views import *

router = DefaultRouter()

router.register(r'review_target', ReviewTargetViewset,
                basename='review_target')
router.register(r'review', ReviewViewset, basename='review')
router.register(r'group', GroupViewset, basename='group')
router.register(r'chart_data', ChartDataViewset, basename='chart_data')

urlpatterns = router.urls


def load_data(request):
    loader.update_all()
    return redirect('/api')


urlpatterns.append(path('load', load_data))
