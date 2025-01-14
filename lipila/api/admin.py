from django.contrib import admin
from .models import (MyUser,
                     Product, LipilaCollection,
                     LipilaDisbursement, BNPL
                     )


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'bio',
                    'address', 'company', 'city', 'country', 'first_name', 'profile_image')


class LipilaCollectionAdmin(admin.ModelAdmin):
    list_display = ('payee', 'payer_account', 'amount', 'timestamp',
                    'reference_id', 'description', 'payer_email',
                    'payer_name', 'status')

    def get_queryset(self, request):
        if request.user.is_superuser:
            return LipilaCollection.objects.all()
        else:
            return LipilaCollection.objects.none()


class DisbursementAdmin(admin.ModelAdmin):
    list_display = ('payer', 'payee', 'payee_account', 'payment_amount', 'payment_method',
                    'description', 'transaction_id', 'payment_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_owner', 'price',
                    'date_created', 'status')

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.none()


class BNPLAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'requested_by',
        'product',
        'amount',
        'status',
        'approved_by'
    )


# Register your models here.
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(LipilaCollection, LipilaCollectionAdmin)
admin.site.register(LipilaDisbursement, DisbursementAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BNPL, BNPLAdmin)

admin.site.site_header = 'Lipila Adminstration'
admin.site.site_url = '/api/v1/index'

# superuser: pita, password: test@123
