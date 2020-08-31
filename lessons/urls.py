from django.urls import path
from .views import LessonListView, LessonDetailView, LessonCreate, LessonUpdate, LessonDelete

lessons_patterns = ([
    path('', LessonListView.as_view(), name='lessons'),
    path('<int:pk>/<slug:slug>/', LessonDetailView.as_view(), name='lesson'),
    path('create/', LessonCreate.as_view(), name='create'),
    path('update/<int:pk>/', LessonUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', LessonDelete.as_view(), name='delete'),
], 'lessons')