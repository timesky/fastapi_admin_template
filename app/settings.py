import os
import sys

# 当前文件和根目录路径
ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_PATH)

from environs import Env
from loguru import logger
from app.extensions.logger_extras import DEFAULT_LOG_FORMAT, log_uid

env = Env()
env.read_env(path=os.path.join(ROOT_PATH, '.env'))

# ========== 环境配置 ==========
LOGS_PATH = env.str("LOGS_PATH", os.path.join(ROOT_PATH, "logs"))

# ========== 日志配置 ==========
logger.remove()
logger.add(
    sys.stderr,
    format=env.str(
        'LOGURU_FORMAT',
        DEFAULT_LOG_FORMAT,
    ),
    backtrace=env.bool('LOGURU_BACKTRACE', True),
    diagnose=env.bool('LOGURU_DIAGNOSE', True),
)
logger.opt(exception=True)
logger.configure(extra={"unique_id": log_uid})

# ========== 数据库配置 ==========

# 异步操作数据库
SQLALCHEMY_DATABASE_URI = env.str(
    'ASYNC_SQLALCHEMY_DATABASE_URI',
    "mysql+aiomysql://root:password@localhost/basename",
)

SQLALCHEMY_ECHO = env.bool('SQLALCHEMY_ECHO', False)
# 每n秒检查一次连接池（重要，可避免链接超时断开）
SQLALCHEMY_POOL_RECYCLE = env.int('SQLALCHEMY_POOL_RECYCLE', 7200)
# 连接池最大连接数
SQLALCHEMY_POOL_SIZE = env.int('SQLALCHEMY_POOL_SIZE', 50)
# 连接池最大等待时间
SQLALCHEMY_POOL_TIMEOUT = env.int('SQLALCHEMY_POOL_TIMEOUT', 30)
# 连接池超出最大连接数时，最大超出上限
SQLALCHEMY_MAX_OVERFLOW = env.int('SQLALCHEMY_MAX_OVERFLOW', 10)

# ========== redis配置 ==========
REDIS_URL = env.str("REDIS_URL", "redis://localhost:6379/1?health_check_interval=60&decode_responses=True")

# ========== api配置 ==========
FASTAPI_INIT_OPTIONS = {
    'docs_url': env.str('FASTAPI_DOCS_URL', '/private/docs'),
    'redoc_url': env.str('FASTAPI_REDOC_URL', '/private/docs2'),
    'openapi_url': env.str('FASTAPI_OPENAPI_URL', '/private/docs/p.json'),
    'swagger_ui_oauth2_redirect_url': env.str('FASTAPI_SWAGGER_UI_OAUTH2_REDIRECT_URL', ''),
}

FASTAPI_CORS_ORIGINS = env.list('CORS_ORIGINS', ['http://localhost:9528', 'http://127.0.0.1:9528'], subcast=str)
