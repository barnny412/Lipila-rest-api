from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     # Public URLS
     path('', views.index, name='index'),
     path('payment/', views.send_money, name='payment'),
     path('service-details/', views.service_details, name='service-details'),
     path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
     path('pages-faq/', views.pages_faq, name='pages-faq'),     
     
     # Auth
     path('signup/', views.SignupView.as_view(), name='signup'),
     path('login/', views.login, name='login'),
     
     # Authenticated User Urls
     path('dashboard/<int:id>', views.dashboard, name='dashboard'),
     path('users-profile/<int:id>', views.users_profile, name='users-profile'),
     path('logout/', views.logout, name='logout'),
     path('bnpl/', views.bnpl, name='bnpl'),
     
     # Logs
     path('transfer-history/', views.log_transfer, name='log_transfer'),
     path('invoice-history/', views.log_invoice, name='log_invoice'),
     path('product-history/', views.log_products, name='log_products'),
     # Actions
     path('invoice/', views.invoice, name='invoice'),
     path('transfer/', views.transfer, name='transfer'),
     path('products/', views.products, name='products'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)