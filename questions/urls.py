from django.urls import path
from .views import QuestionsView, TitleListView, QuestionsDetailView, CleanTextAPIView

urlpatterns = [
    path('', QuestionsView.as_view(), name='questions'),
    path('titles/', TitleListView.as_view(), name='titles'),
    path('details/<int:no>', QuestionsDetailView.as_view(), name = 'details'),
    path('answer/', CleanTextAPIView.as_view(), name = 'answer')
]