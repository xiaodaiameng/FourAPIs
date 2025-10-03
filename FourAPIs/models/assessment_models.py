from typing import List, Dict, Optional
from pydantic import BaseModel

# 数据模型定义
class UserAnswer(BaseModel):
    question_id: int
    option_id: str

class AssessmentRequest(BaseModel):
    major: str
    answers: List[UserAnswer]

class CareerRecommendation(BaseModel):
    career: str
    description: str

class AssessmentResult(BaseModel):
    user_major: str
    dominant_traits: List[str]
    recommended_careers: List[CareerRecommendation]

class ReportSection(BaseModel):
    title: str
    content: str

class AssessmentReport(BaseModel):
    result: AssessmentResult