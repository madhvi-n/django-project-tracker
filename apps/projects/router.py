from rest_framework_nested import routers

from projects.views import ProjectViewSet
from boards.views import BoardViewSet, BoardSectionViewSet
from tasks.views import TaskViewSet, TaskTypeViewSet

router = routers.SimpleRouter()

router.register(r'projects', ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'boards', BoardViewSet)
project_router.register(r'task_types', TaskTypeViewSet)

board_router = routers.NestedSimpleRouter(project_router, r'boards', lookup='board')
board_router.register(r'sections', BoardSectionViewSet)

section_router = routers.NestedSimpleRouter(board_router, r'sections', lookup='section')
section_router.register(r'tasks', TaskViewSet)
