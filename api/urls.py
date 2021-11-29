from django.urls import path
from .views import GenerateActivity, CategoryList, RetrieveActivity

urlpatterns = [
    path('generate_activity/', GenerateActivity.as_view(), name="generate_activity"),
    path('get_categories/', CategoryList.as_view(), name="catagory_list"),
    path('get_activity/', RetrieveActivity.as_view(), name="get_activity"),
]