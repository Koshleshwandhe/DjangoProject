from django.urls import path
from .views import UserListView, UserDetailView, ExpenseListView, ExpenseDetailView, ParticipantListView, ParticipantDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('participants/', ParticipantListView.as_view(), name='participant-list'),
    path('participants/<int:pk>/', ParticipantDetailView.as_view(), name='participant-detail'),
]
