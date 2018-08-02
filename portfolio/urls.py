from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('blog/', include('blog.urls')) #? What this does is tell django that whenever somebody goes to website/blog/whatever to send them or forward them to the urls.py in the blog app file

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #this is where you should look for the information
