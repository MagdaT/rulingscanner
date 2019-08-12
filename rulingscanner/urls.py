from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from rulingscanner.views import main_page, like_post, RulingDetailView, register_view, trends, last_added, \
     SearchRulingView

app_name = 'rulingscanner'
urlpatterns = [

    path('', main_page, name='main-page'),
    path('main_page/', main_page, name='main-page'),
    path('hints/', main_page, name='hints'),
    path('forum/', main_page, name='forum'),
    path('profile/', main_page, name='profile'),
    path( 'accounts/profile/', main_page, name='profile' ),
    path('compose/', main_page, name='compose'),
    path(r'^like/$', like_post, name="like-post"),
    path('ruling_details/<int:pk>', RulingDetailView.as_view(),
         name='hint-detail' ),
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'),
         name='password-reset'),
    path('register/', register_view, name='register'),
    # path('trends/', trends, name='trends'),
    path('search/', SearchRulingView.as_view(), name='search-ruling'),
    path('last_added/', last_added, name='last_added'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
