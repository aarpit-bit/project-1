from django.urls import path, include
from rest_framework import routers
from .views import *

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register('employee_details', EmployeeViewset)

router.register('company_details', CompanyViewset)

router.register('project_details', ProjectViewset)


urlpatterns=[
    path('api/',include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)