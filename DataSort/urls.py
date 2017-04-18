from django.conf.urls import *
from DataSort import views
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.conf.urls.static import static

app_name = "DataSort"

urlpatterns = [
    url(r'^$',views.result,name='result'),
    #url(r'^result/$',views.result,name='result'),
    url(r'^plot/([0-9]+)/$',views.plot,name='plot')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)