from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^runhist/$', views.RunHistoryListView.as_view(), name='rh_list'),
    url(r'^ajax/update_rv$', views.update_rv, name='rv_update'),
    url(r'^$', views.get_rh),
]
