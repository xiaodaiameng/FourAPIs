from fastapi import FastAPI


def register_routes(app: FastAPI):

    from api.holland_questions import questions_router
    from api.holland_calculate_results import results_router
    from api.holland_assessment_submit import assessment_router
    # from api.random3careers import random3careers_router

    app.include_router(questions_router, prefix="/api")
    app.include_router(results_router, prefix="/api")
    app.include_router(assessment_router, prefix="/api")
    # app.include_router(random3careers_router, prefix="/api")