class IncludeAPIRouter(object):
    def __new__(cls):
        from app.routes.hello_world import router as router_hello_world
        from fastapi.routing import APIRouter
        router = APIRouter()

		# Import other routes below
        router.include_router(router_hello_world,
                              prefix='/api/v1', tags=['Hello World'])
        return router

