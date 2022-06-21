from django.urls import path
from webapp.views import guess
from webapp.views import view_history


urlpatterns = [
    path('', guess),
    path('history.html', view_history)
]
