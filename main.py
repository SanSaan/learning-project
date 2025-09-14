from urllib import request

from fastapi import FastAPI
import logging

from config import log_config


# Apply the configuration
log_config.setup_logging()

# Create a logger instance
logger = logging.getLogger("app")

app = FastAPI()


@app.get("/")
async def root():
    logger.info("root endpoint")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    logger.info("Hello %s", name)
    return {"message": f"Hello {name}"}
