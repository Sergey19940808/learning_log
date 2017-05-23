# urls for application learning_logs
from django.conf.urls import url
from . import views

# urls apps users
urlpatterns = [
    url(r'^user/(?P<user_id>\d+)/$', views.user, name='user'),
    url(r'^resend_activation_email/$', views.resend_activation_email,
        name='resend_activation_email'),
    url(r'^email_change/(?P<user_id>\d+)/$', views.email_change, name='email_change'),
    url(r'^add_first_last_name/(?P<user_id>\d+)/$', views.add_first_last_name,
        name='add_first_last_name'),
    url(r'^edit_first_last_name/(?P<user_id>\d+)/$', views.edit_first_last_name,
        name='edit_first_last_name'),
    url(r'^delete_user/(?P<user_id>\d+)/$', views.delete_user, name='delete_user')
]
