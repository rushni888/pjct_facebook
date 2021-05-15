from django.urls import path
from . import views

urlpatterns = [    
    path('index/',views.index,name='index'),
    path('login',views.login,name='login'),
    path('forgotpass',views.forgotpass,name='forgotpass'),
    path('bootstrapgrid',views.bootstrapgrid,name='bootstrapgrid'),
    path('fbhome',views.fbhome,name='fbhome'),
    path('samplejs',views.samplejs,name='samplejs'),
    path('navbar',views.navbar,name='navbar'),
    path('home',views.home,name='home'),
    path('jquery',views.jquery,name='jquery'),
    path('dynamicdata1',views.dynamicdata1,name='dynamicdata1'),
    path('dynamicdata2',views.dynamicdata2,name='dynamicdata2'),
    path('signup',views.signup,name='signup'),
    path('layout',views.layout,name='layout'),
    path('viewprofile',views.viewprofile,name='viewprofile'),
    path('file',views.file1,name='file'),
    # path('fbhomedummy',views.fbhomedummy,name='viewprofile'),
    
]
