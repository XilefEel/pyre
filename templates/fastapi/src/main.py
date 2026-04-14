from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.session import create_tables
from routes.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    create_tables()
    yield


app = FastAPI(
    title="{project_name}",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(users_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": "{project_name}"}
