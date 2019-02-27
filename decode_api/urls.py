from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("profile", views.UserProfileViewSet)  # Model view Set so no base name
router.register('login', views.LoginViewSet, base_name= 'login')
urlpatterns = [
    url(r'',include(router.urls)),
    url(r'^leaderboard/',views.LeaderBoardView.as_view()),
    url(r'^problem/(?P<pk>\d+)/$', views.ProblemApiDetail.as_view()),
    url(r'^problem/$', views.ProblemApi.as_view()),
    url(r'^solution/(?P<pk>\d+)/$', views.SolutionApiDetail.as_view()),
    url(r'^solution/$', views.SolutionApi.as_view()),
    url(r'^stats/(?P<pk>\d+)/$', views.StatsApiDetail.as_view()),
    url(r'^stats/$', views.StatsApi.as_view()),
]