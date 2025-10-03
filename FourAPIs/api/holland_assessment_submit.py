from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.holland_calculate_results import calculate_assessment_result
from models.assessment_models import AssessmentRequest, AssessmentResult
from config.database_config import get_db
from repository.assessment_repository import AssessmentRepository

# 使用一致的路由对象名称
assessment_router = APIRouter(prefix="/assessment", tags=["assessment"])
# 为了保持与api/__init__.py的兼容性
router = assessment_router

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
    return {"username": "anonymous", "role": "guest"}

@assessment_router.post("/submit", response_model=AssessmentResult)
def submit_assessment(
    request: AssessmentRequest,
    current_user: dict = Depends(get_current_user),
    db = Depends(get_db)
):
    try:

        result = calculate_assessment_result(request, db)

        if result.result.dominant_traits and len(result.result.dominant_traits) > 0:
            traits_combined = ''.join(result.result.dominant_traits[:2])

            db_result = AssessmentRepository.create_assessment_result(db, traits_combined)            #
            print(f"测评结果已保存到数据库，ID: {db_result.id}, 结果: {db_result.result}")
        else:
            print("未找到有效的特质数据，结果未保存到数据库")
            print(f"当前result对象: {result}")
            print(f"result.result: {result.result}")
        return result.result
    except HTTPException as e:
        print(f"HTTP异常: {str(e)}")
        raise
    except Exception as e:
        print(f"保存结果时发生错误: {str(e)}")
        raise HTTPException(status_code=500, detail=f"提交答案失败: {str(e)}")


@assessment_router.get("/results", tags=["assessment", "results"])
def get_all_assessment_results( db = Depends(get_db), skip: int = 0, limit: int = 100):
    try:
        results = AssessmentRepository.get_all_assessment_results(db, skip, limit)
        return [{
            "id": result.id,
            "result": result.result
        } for result in results]# 转为字典
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取测评结果失败: {str(e)}")

