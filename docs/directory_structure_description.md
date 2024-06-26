目录结构说明
---

- 项目根目录结构说明
  - **run.py**： 程序主入口文件，包括api
  - **.gitignore**： git忽略列表
  - **README.md**： 项目说明入口文件
  - **requirements.txt**： 项目依赖列表
  - **app**: 项目源码存放目录
    - clients: 爬虫类，对应单接口级别的抓取类
    - cores: 核心代码，主要是核心的父类，共外部继承
    - extensions: 对第三方依赖的二次包装，如数据库，redis等
    - models: 数据库orm模型
    - services: 业务逻辑存放位置
    - views: 接口类存放位置
  - **docs**: 项目说明文档存放目录