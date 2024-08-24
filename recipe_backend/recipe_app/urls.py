from django.urls import path
from .views import RandomDishView, CookingTimerView

urlpatterns = [
    path('random-dish/', RandomDishView.as_view(), name='random_dish'),
    path('start-timer/', CookingTimerView.as_view(), name='start_timer'),
]