from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'payments', views.LipilaCollectionView, basename='payments')
router.register(r'products', views.ProductView, basename='products')
router.register(r'signup', views.SignupViewSet, basename='signup')
router.register(r'profile', views.ProfileView, basename='profile')
router.register(r'bnpl', views.BNPLView, basename='bnpl')

urlpatterns = [
     path('login/', views.LoginView.as_view(), name='api-login'),
]

urlpatterns += router.urls

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

# handler404 = 