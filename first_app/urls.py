from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from first_app import views

app_name='link'

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^signup/$',views.signupforms, name='signup'),
    url(r'^signupw/$',views.signupw, name='signupw'),
    url(r'^signin/$',views.signin, name='signin'),
    url(r'^content/$',views.content, name='content'),
    url(r'^postad/$',views.adposting, name='postad'),
    url(r'^show_ads/$',views.show_ads, name='show'),
    url(r'^addetails/$',views.addetails, name='addetails'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    url(r'^hell/$',views.hell, name='hell'),
    url(r'^aiding/$',views.aiding, name='aiding'),
    url(r'^Divission/$',views.divissionadd, name='divissionadd'),
    url(r'^search/$',views.search, name='search'),
    url(r'^tattadaa/$',views.tattadaa, name='tattadaa'),



#   url(r'^middetails/$',views.middetails, name='middetails'),


    #url(r'^signin/$',views.signinforms, name='signin'),



]
