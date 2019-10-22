from rest_framework.routers import SimpleRouter

from DjangoFood.views import Foods_View

router = SimpleRouter()
router.register(r"API/Foods",Foods_View)