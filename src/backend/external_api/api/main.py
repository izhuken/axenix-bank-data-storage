from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import (
    accept_report_router,
    create_report_router,
    new_user_router,
    search_router,
    upload_database_router,
    user_external_report_router,
    user_internal_report_router,
)

app = FastAPI(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accept_report_router, prefix="/v1")
app.include_router(search_router, prefix="/v1")
app.include_router(create_report_router, prefix="/v1")
app.include_router(user_external_report_router, prefix="/v1")
app.include_router(user_internal_report_router, prefix="/v1")
app.include_router(new_user_router, prefix="/v1")
app.include_router(upload_database_router, prefix="/v1")
