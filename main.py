import uvicorn
from app.config import config

if __name__ == "__main__":
    uvicorn.run(
        app="manage:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=config.ENV != "prod",
        workers=1,
    )
