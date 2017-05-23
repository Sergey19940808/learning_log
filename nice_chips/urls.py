# urls for application nice_chips
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import IndexDraftView, IndexReminderView, DraftAddView, ReminderAddView

# urls
urlpatterns = [
    url(r'^index_draft/$', login_required(IndexDraftView.as_view
                                          (template_name = 'nice_chips/draft/index_draft.html')),
                                          name='index_draft'),
    url(r'^add_draft/$', login_required(DraftAddView.as_view()), name='add_draft'),
    url(r'^edit_draft/(?P<draft_id>\d+)/$', views.edit_draft, name='edit_draft'),
    url(r'^delete_draft/(?P<draft_id>\d+)/$', views.delete_draft, name='delete_draft'),
    url(r'^index_reminder/$', login_required(IndexReminderView.as_view()), name='index_reminder'),
    url(r'^add_reminder/$', login_required(ReminderAddView.as_view()), name='add_reminder'),
]