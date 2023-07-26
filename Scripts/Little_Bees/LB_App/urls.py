from django.urls import path
from . import views

urlpatterns = [
    path('LB_App/',views.index,name='index'),
    path('LB_App/index',views.index,name='index'),
    path('', views.index, name='index'),
    path('LB_App/about',views.about,name='about'),
    path('LB_App/classes',views.classes,name='classes'),
    path('LB_App/gallery',views.gallery,name='gallery'),
    path('LB_App/infos_utiles',views.infos_utiles,name='infos_utiles'),
    path('tri_enfants_table/', views.tri_enfants_table, name='tri_enfants_table'),
    path('tri_mention_table/', views.tri_mention_table, name='tri_mention_table'),
    path('LB_App/resultats',views.resultats,name='resultats'),
    path('LB_App/contact',views.contact,name='contact'),
    path('LB_App/call-to-action',views.call_to_action,name='call-to-action'),
]