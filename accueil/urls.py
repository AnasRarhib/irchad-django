from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="accueil"),
    path("Inscription/",views.inscription, name="inscription"),
    path("Se-Connecter/",views.seConnecter,name="seConnecter"),
    path("Deconnection/",views.deconnection,name="deconnection"),
    path("Irchad/<str:session_id>",views.irchad,name="irchad"),
    path('getMessages/<str:session_id>', views.getMessages, name='getMessages'),
    path('send',views.send,name="send"),
    path('listSessions',views.listSessions,name="listSessions"),
    path('listSessions/sessionRh/<str:session_id>',views.sessionRh,name='sessionRh'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)