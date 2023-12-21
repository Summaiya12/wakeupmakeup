from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home', views.Index, name='home'),
                  path('about/', views.About, name='about'),
                  path('cart/<int:product_id>', views.Carts, name='cart'),
                  path('show_cart/', views.Show_cart, name='show_cart'),
                  path('remove/<int:item_id>/', views.Remove_cart, name='remove_cart'),
                  path('checkout/<int:product_id>', views.Checkout, name='checkout'),
                  path('show_check/', views.Show_check, name='show_check'),
                  path('client/', views.Client, name='client'),
                  path('contact/', views.Contact, name='contact'),
                  path('login/', views.Login, name='login'),
                  path('products/', views.Products, name='products'),
                  path('', views.Register, name='register'),
                  path('logs/', views.Logs, name='logs'),
                  path('profile/', views.Profile, name='profile'),
                  path('address/', views.Address, name='address'),
                  path('action/', views.Action, name='action'),
                  path('update/<int:pk>', views.Update, name='update'),
                  path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
                  path('detail/<int:product_id>', views.Detail, name='detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
