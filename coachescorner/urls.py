"""coachescorner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


from coachescornerapi.views.auth import login_user,register_Player,register_coach
from coachescornerapi.views.coach import CoachView
from coachescornerapi.views.college import CollegeView
from coachescornerapi.views.game import GameView
from coachescornerapi.views.open_spot import OpenSpotView
from coachescornerapi.views.player import PlayerView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'players', PlayerView, 'player')
router.register(r'games', GameView, 'game')
router.register(r'open_spots', OpenSpotView, 'open_spot')
router.register(r'coaches', CoachView, 'coach')
router.register(r'colleges', CollegeView, 'college')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('registerPlayer', register_Player),
    path('registerCoach', register_coach),
    
    path('', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
