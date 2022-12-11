from django.urls import include, path

from projects.router import (
    router,
    project_router,
    board_router,
    section_router
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(project_router.urls)),
    path('api/v1/', include(board_router.urls)),
    path('api/v1/', include(section_router.urls)),
]
