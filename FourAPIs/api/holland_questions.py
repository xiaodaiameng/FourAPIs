from fastapi import APIRouter, HTTPException, Depends
from models.database_models import AssessmentQuestionDB
from config.database_config import get_db
from sqlalchemy.orm import Session

questions_router = APIRouter(prefix="/assessment/questions", tags=["assessment", "questions"])

@questions_router.get("/")
def get_assessment_questions(db: Session = Depends(get_db)):
    db_questions = db.query(AssessmentQuestionDB).all()
    result_questions = []
    for db_question in db_questions:
        result_questions.append({
            "id": db_question.id,
            "question": db_question.question_text,
            "options": db_question.options
        })
    return result_questions

@questions_router.get("/{question_id}")
def get_assessment_question(question_id: int, db: Session = Depends(get_db)):
    db_question = db.query(AssessmentQuestionDB).filter(AssessmentQuestionDB.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail=f"未找到ID为{question_id}的问题")
    return {
        "id": db_question.id,
        "question": db_question.question_text,
        "options": db_question.options
    }

@questions_router.get("/count")
async def get_questions_count(db: Session = Depends(get_db)):
    count = db.query(AssessmentQuestionDB).count()
    return {"count": count}


def get_holland_questions_data(db: Session = None):
    if db is None:
        db = next(get_db())
        try:
            return get_assessment_questions(db)
        finally:
            db.close()
    else:
        return get_assessment_questions(db)

def get_holland_question_by_id(question_id: int, db: Session = None):
    if db is None:
        db = next(get_db())
        try:
            db_question = db.query(AssessmentQuestionDB).filter(AssessmentQuestionDB.id == question_id).first()
        finally:
            db.close()
    else:
        db_question = db.query(AssessmentQuestionDB).filter(AssessmentQuestionDB.id == question_id).first()
    if not db_question:
        raise ValueError(f"未找到ID为{question_id}的问题")
    
    return {
        "id": db_question.id,
        "question": db_question.question_text,
        "options": db_question.options
    }