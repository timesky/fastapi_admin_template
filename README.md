机票Booking模块
---

> - 基础数据抓取
> - 基础数据查询接口
> - 预订流程相关接口及脚本

## [目录结构说明](docs/directory_structure_description.md)

## 运行条件
> 列出运行该项目所必须的条件和相关依赖  
- 注意
  - uvicorn依赖包的安装方式，必须指定[standard]安装，这样才能让性能与uwsgi基本一致，standard方式安装的uvicorn是基于cpython优化的版本




## 运行说明
> 说明如何运行和使用你的项目，建议给出具体的步骤说明

- 启动非api脚本、任务等

```bash
python run.py 命令名称
```

- 启动api
    - 开发环境
    ```bash
    uvicorn --port 8080 --host 0.0.0.0 --reload run:fast_api_app
    ```
    - 生产环境

    ```bash
    uvicorn --port 8080 --host 0.0.0.0 run:fast_api_app  --workers 4 --loop uvloop --http httptools
    ```


## 测试说明
> 如果有测试相关内容需要说明，请填写在这里  



## 技术架构
> 使用的技术框架或系统架构图等相关说明，请填写在这里  


## 协作者
> 高效的协作会激发无尽的创造力，将他们的名字记录在这里吧
