import asyncio
from app import settings

import typer
from app.api import fast_api_app

cli = typer.Typer()


# @cli.command()
# def api(host: str = '0.0.0.0', port: int = 8080):
#     """运行api

#     开发调试
#     """
#     import uvicorn

#     uvicorn.run(fast_api_app, host=host, port=port)


@cli.command()
def debug():
    """调试"""
    # asyncio.run()
    pass


if __name__ == '__main__':
    cli()
