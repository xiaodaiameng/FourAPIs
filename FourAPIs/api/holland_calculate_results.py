from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Optional
import random
from sqlalchemy.orm import Session
from config.database_config import get_db
from data.holland_careers import HOLLAND_CAREERS
from data.major_career_mapping import get_major_related_careers, calculate_career_match_score, get_career_description
from api.holland_questions import get_holland_questions_data
from repository.assessment_repository import AssessmentRepository
from models.assessment_models import AssessmentRequest, AssessmentResult, CareerRecommendation, AssessmentReport

results_router = APIRouter(prefix="/assessment/results", tags=["assessment", "results"])

@results_router.post("/calculate", response_model=AssessmentReport)
def calculate_assessment_result(request: AssessmentRequest, db: Session = Depends(get_db)):
    questions = get_holland_questions_data(db)

    if len(request.answers) != len(questions):
        raise HTTPException(status_code=400, detail="答案数量不正确")

    trait_scores = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
    
    for answer in request.answers:
        question_ids = [q["id"] for q in questions]
        if answer.question_id not in question_ids:
            raise HTTPException(status_code=400, detail=f"无效的问题ID: {answer.question_id}")
        if answer.option_id not in trait_scores.keys():
            raise HTTPException(status_code=400, detail=f"无效的选项ID: {answer.option_id}")
        trait_scores[answer.option_id] += 1
    sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)
    dominant_traits = [trait for trait, _ in sorted_traits[:2]]
    recommended_careers = []
    career_set = set()
    major_related_careers = get_major_related_careers(request.major)
    career_scores = []
    for career in major_related_careers:
        match_score = calculate_career_match_score(career, trait_scores)
        random_factor = random.uniform(0.9, 1.1)
        final_score = match_score * random_factor
        career_scores.append((career, final_score))
    for trait in trait_scores.keys():
        # 从数据库获取该特质对应的职业
        trait_careers = AssessmentRepository.get_careers_by_code(db, trait)
        for career in trait_careers:
            if career not in major_related_careers:
                match_score = calculate_career_match_score(career, trait_scores)
                random_factor = random.uniform(0.9, 1.1)
                final_score = match_score * random_factor
                career_scores.append((career, final_score))
    # 按照匹配度分数排序，选择前10个职业
    career_scores.sort(key=lambda x: x[1], reverse=True)
    selected_careers = []
    for career, _ in career_scores:
        if career not in career_set and len(selected_careers) < 5:
            career_set.add(career)
            description = get_career_description(career, request.major, trait_scores)
            selected_careers.append(
                CareerRecommendation(
                    career=career,
                    description=description
                )
            )
    if len(selected_careers) < 5:
        # 从所有职业中随机选择一些作为补充
        all_careers = list(set(major_related_careers + [career for sublist in HOLLAND_CAREERS.values() for career in sublist]))
        random.shuffle(all_careers)
        
        for career in all_careers:
            if career not in career_set and len(selected_careers) < 5:
                career_set.add(career)
                description = get_career_description(career, request.major, trait_scores)
                selected_careers.append(
                    CareerRecommendation(
                        career=career,
                        description=description
                    )
                )
    
    # 再次打乱顺序
    random.shuffle(selected_careers)

    assessment_result = AssessmentResult(
        user_major=request.major,
        dominant_traits=dominant_traits,
        recommended_careers=selected_careers
    )
    return AssessmentReport(result=assessment_result)