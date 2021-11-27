from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path ("about/", views.about, name="about"),
    path('search/', views.post_search, name='post_search'),
    path('<slug:motorcycle>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
