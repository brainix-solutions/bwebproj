from django .urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('success/',views.success, name='success'),
    path('trial_workshop_registration_success/',views.trial_workshop_registration_success, name='trial_workshop_registration_success'),
    path('failed/',views.failed, name='failed'),
    path('gallery/',views.gallery, name='gallery'),
    path('pay/',views.pay, name='pay'),
    path('gallery1/',views.gallery1, name='gallery1'),
    path('workshop/',views.workshop,name='workshop'),
    path('checkout/<str:pk_test>',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('free-register/',views.trial_form,name='trial_form'),
    path('online science workshop/',views.pay_form,name='pay_form'),
    path('test/',views.testpage, name='test'),
    ]