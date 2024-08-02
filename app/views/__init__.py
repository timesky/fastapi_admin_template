def register_routes(app):
    # 注意在方法内部引入需要的模块
    # 避免引发循环导入

    from . import demo_views

    app.include_router(demo_views.routers)
