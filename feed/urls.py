from django.conf.urls import url
from . import views


app_name = 'feed'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^keyword/(?P<keyword>\w+)/$', views.FindKeyWordNews.as_view(), name='keyword'),
    url(r'^keyword/$', views.FindKeyWordNews.as_view(), name='keyword'),
    url(r'^news$', views.news, name='news'),
    url(r'^stats$', views.stats, name='stats'),
    url(r'^republic$', views.republic, name='republic'),
    url(r'^ndtv$', views.ndtv, name='ndtv'),
    url(r'^indiatoday$', views.indiatoday, name='indiatoday'),
    url(r'^hindustan$', views.hindustan, name='hindustan'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^signup$', views.SignUpForm.as_view(), name='signup'),
    url(r'^newsAPI/$', views.NewsList.as_view(), name='newsAPI'),

]
