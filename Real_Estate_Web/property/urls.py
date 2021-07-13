
from django.urls import path
from . import views
from .views import residential_property_update, pg_property_update, plot_property_update, commercial_property_update

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('property-create/', views.property_create, name='property-create'),
    path('property-create/<str:form_type>', views.property_create, name='property-create'),
    path('update/<int:pk>/residential', residential_property_update.as_view(), name='residential-property-update'),
    path('update/<int:pk>/commercial', commercial_property_update.as_view(), name='commercial-property-update'),
    path('update/<int:pk>/plot', plot_property_update.as_view(), name='plot-property-update'),
    path('update/<int:pk>/pg', pg_property_update.as_view(), name='pg-property-update'),
    path('delete/<int:property_id>/<str:property_type>', views.property_delete, name='property-delete'),
    path('upload-image/<int:property_id>/<str:property_type>', views.property_image_upload, name='property-image-upload'),
    path('property-list/', views.property_list, name='property-list'),
    path('property-single/<int:property_id>/<str:property_type>', views.property_single, name='property-single'),
    path('agent-single/<int:user_id>/', views.agent_single, name='agent-single'),
    path('agent-list/', views.agent_list, name='agent-list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('property-create-partial/', views.property_create_partial, name='property-create-partial')
]
