from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)
from .views import public_api, protected_api , list_telegram_users , simulate_start

urlpatterns = [
    path('public/', public_api),
    path('protected/', protected_api),

    # ✅ JWT login renamed to /login/
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # ✅ JWT token refresh
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   

    path('telegram-users/', list_telegram_users),
    path('simulate-start/', simulate_start),

]

