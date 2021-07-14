import uvicorn
import subprocess
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.utils.logger import Logging
from app.utils.exceptions import CustomException
from app.initializer import IncludeAPIRouter
from app.config import config

def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Error Handling
def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

# Initialize APP
def get_application():
    _app = FastAPI(title=config.API_NAME,
                   description=config.API_DESCRIPTION,
                   version=config.API_VERSION,
                   dependencies=[Depends(Logging)],)
    _app.include_router(IncludeAPIRouter())
    init_cors(app=_app)
    init_listeners(app=_app)
    return _app


app = get_application()


@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    print("On App Shutdown i will be called.")
