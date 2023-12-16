from django.urls import path
from .views import Listview,DetailView
# urlpatterns = [
#     path('',home,name='home'),
#     path("product/<int:id>",single,name="product")

# ]





urlpatterns=[
    path('',Listview.as_view(),name='home'),
    path("product/<int:pk>/",DetailView.as_view(), name="product")
]