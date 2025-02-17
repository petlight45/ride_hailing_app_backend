from utils.router import RouterUtils

from ..views import guest as views

router = RouterUtils.get_router()

router.register("", views.RidePricingViewSet, basename="app_ride_pricing")

urlpatterns = router.urls
