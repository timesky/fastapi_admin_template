from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app import settings


routers = APIRouter(prefix=f'{settings.API_PERFIX}/demo', tags=['管理账号接口'])


# 普通接口
@routers.post(
    "/hello",
    summary="hello接口",
)
async def hello():
    return {"message": "Hello World"}


# 报错实例
@routers.post(
    "/error",
    summary="error接口",
)
async def error():
    raise HTTPException(status_code=500, detail="Internal server error")


# 用model约束输入输出
class DemoReq(BaseModel):
    id: int


class DemoResp(BaseModel):
    data: str


@routers.post("/demo", summary="demo接口", response_model=DemoResp)
async def demo(req: DemoReq):
    return DemoResp(data=f"hello {req.id}")
