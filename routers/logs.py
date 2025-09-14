import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()

async def log_streams():
    with open("fastapi.log") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                await asyncio.sleep(0.1)


@router.get("/logs/tail")
async def tail_logs():
    return StreamingResponse(log_streams(), media_type="text/event-stream")