from django.urls import path
from .views import Questionnaire_view, success_view

urlpatterns = [
    path("", Questionnaire_view, name="Questionnaire"),
    path("success/", success_view, name="success"),
]
