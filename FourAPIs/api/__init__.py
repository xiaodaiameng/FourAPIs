# API模块统一导出
from .holland_questions import questions_router
from .holland_calculate_results import results_router
from .holland_assessment_submit import router as assessment_router

__all__ = ["questions_router", "results_router", "assessment_router"]