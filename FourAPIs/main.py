from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from deps.api_registry import register_routes  # 从 deps 导入
from repository.database_init import init_database

app = FastAPI(title="霍兰德职业兴趣测评系统", description="提供霍兰德职业兴趣测评的完整功能")

app.mount("/static", StaticFiles(directory="static"), name="static")

# 传入recreate_tables=True来重新创建数据库表
success = False
try:
    init_database(recreate_tables=True)
    success = True
    print("数据库初始化成功")
except Exception as e:
    print(f"数据库初始化异常: {str(e)}")

# 如果初始化失败，尝试不重新创建表
if not success:
    try:
        print("尝试不重新创建表进行初始化...")
        init_database(recreate_tables=False)
        print("数据库初始化成功")
    except Exception as e:
        print(f"数据库初始化再次失败: {str(e)}")
        print("应用程序可能会正常运行，但某些功能可能受限")

register_routes(app)

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.get("/assessment.html")
def read_assessment_html():
    return FileResponse("static/assessment.html")

@app.get("/random3careers.html")
def read_random3careers_html():
    return FileResponse("static/random3careers.html")

@app.get("/health")
def health_check():
    return {
        "status": "running",
        "system": "霍兰德职业兴趣测评系统",
        "docs": "/docs"
    }