from django.urls import path
from .views import GenerateActivity, CategoryList, RetrieveActivity, RetrieveDescendingActivity

urlpatterns = [
    path('generate_activity/', GenerateActivity.as_view(), name="generate_activity"),
    path('get_categories/', CategoryList.as_view(), name="catagory_list"),
    path('get_activity/', RetrieveActivity.as_view(), name="get_activity"),
    path('get_activity/desc/', RetrieveDescendingActivity.as_view(), name="get_activity_descending"),
]