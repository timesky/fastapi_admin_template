import time
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger


from app.views import register_routes
from app import settings


fast_api_app = FastAPI(
    default_response_class=ORJSONResponse,
    **settings.FASTAPI_INIT_OPTIONS,
)


@fast_api_app.middleware("http")
async def log_requests(request: Request, call_next):
    from app.extensions.logger_extras import log_uid

    request_id = str(uuid.uuid4())  # 生成唯一的请求ID

    log_uid.set(request_id)  # 给日志增加唯一标识

    request.state.request_id = request_id

    start_time = time.time()
    # logger.info(f"Request start {request_id} [{request.method}] {request.url.path}")
    response = await call_next(request)
    process_time = time.time() - start_time

    # 在请求处理完成后记录详细的日志，包括请求ID、路径、方法和耗时
    log_details = {
        "request_id": request_id,
        "path": request.url.path,
        "method": request.method,
        "request": request,
        "response": response,
        "request_time": round(process_time, 8),
    }
    # logger.info(f"Request end {request_id} {round(process_time, 8)}: {response.status_code} {log_details}")
    logger.info(f"Request end {log_details}")
    # 将请求ID添加到响应头中，可选
    response.headers['X-Request-ID'] = request_id

    return response


fast_api_app.add_middleware(
    CORSMiddleware,
    # 这里配置允许跨域访问的前端地址
    allow_origins=settings.FASTAPI_CORS_ORIGINS,
    # 跨域请求是否支持 cookie， 如果这里配置true，则allow_origins不能配置*
    allow_credentials=True,
    # 支持跨域的请求类型，可以单独配置get、post等，也可以直接使用通配符*表示支持所有
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routes(fast_api_app)

__ALL__ = ['fast_api_app']
