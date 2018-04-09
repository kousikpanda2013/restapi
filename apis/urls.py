from django.urls import path
from .views import UserRetrieveCreateList, UserDetail

app_name = 'apis'

urlpatterns = [
    path('', UserRetrieveCreateList.as_view(), name='user-list'),
    path('<int:pk>', UserDetail.as_view(),
         name='user-detail'),
]
