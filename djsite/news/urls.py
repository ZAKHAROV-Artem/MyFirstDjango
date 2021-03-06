from django.urls import path
from news.views import index, get_category

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
]
