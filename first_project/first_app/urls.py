# from django.conf.urls import url
from django.urls import include, re_path as url
from first_app import views

app_name = 'first_app'

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

urlpatterns = [
    url('register/', views.register, name='register'),
    url('user_login/',views.user_login,name='user_login'),
]
