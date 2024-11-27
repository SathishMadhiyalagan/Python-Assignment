from django.urls import path
from .views import etl_process, retrieve_data

urlpatterns = [
    path('etl-process/', etl_process, name='etl_process'),
    path('retrieve-data/', retrieve_data, name='retrieve_data'),
]
