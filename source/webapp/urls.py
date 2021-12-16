from django.urls import path

from webapp.views import index_view, calculations

urlpatterns = [
    path('', calculations)
]