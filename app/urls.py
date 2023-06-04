from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm

urlpatterns = [
    path("",views.home),
    path("category/<slug:val>",views.category.as_view(),name="category"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path("category-title/<val>",views.categoryTitle.as_view(),name="category-title"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("address/",views.address,name="address"),
    path("updateAddress/",views.updateAddress.as_view(),name='updateAddress'),

    #login authentication
    path("customerRegistration/",views.CustomerRegistrationView.as_view(),name="customerRegistration"),
    path('login/',auth_view.LoginView.as_view(template_name="login.html",authentication_form=LoginForm) , name='login'),
    #path('password-reset/',auth_view.PasswordResetView.as_view(template_name="password_reset.html",form_class=MyPasswordResetForm), name='password-reset'),
    #path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name="changepassword.html",form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    #path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name="passwordchangedone.html",form_class=MyPasswordChangeForm), name='passwordchangedone'),
    
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name="changepassword.html", success_url='/passwordchangedone'), name='passwordchange'),
    
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name="passwordchangedone.html"), name='passwordchangedone'),
    
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart',views.show_cart,name='showcart'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)