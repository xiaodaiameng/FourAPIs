from sqlalchemy.orm import Session
from typing import Optional, List, Dict
from models.database_models import AssessmentResultDB, AssessmentQuestionDB, HollandCareerDB


class AssessmentRepository:
    """测评仓库类，提供测评结果、问题和职业数据的CRUD操作"""
    @staticmethod
    def create_assessment_result(db: Session, traits: str) -> AssessmentResultDB:
        """创建一个新的测评结果记录"""
        traits = traits[:2] if traits else ""
        db_result = AssessmentResultDB(result=traits)
        db.add(db_result)
        db.commit()
        db.refresh(db_result)
        
        return db_result

    @staticmethod
    def get_assessment_result(db: Session, result_id: int) -> Optional[AssessmentResultDB]:
        """根据ID获取测评结果记录"""
        return db.query(AssessmentResultDB).filter(AssessmentResultDB.id == result_id).first()

    @staticmethod
    def get_all_assessment_results(db: Session, skip: int = 0, limit: int = 100) -> List[AssessmentResultDB]:
        """获取所有测评结果记录"""
        return db.query(AssessmentResultDB).offset(skip).limit(limit).all()

    @staticmethod
    def update_assessment_result(db: Session, result_id: int, new_traits: str) -> Optional[AssessmentResultDB]:
        """更新测评结果记录"""
        new_traits = new_traits[:2] if new_traits else ""
        db_result = db.query(AssessmentResultDB).filter(AssessmentResultDB.id == result_id).first()
        if db_result:
            db_result.result = new_traits
            db.add(db_result)  # 添加到会话
            db.commit()
            db.refresh(db_result)
        return db_result

    @staticmethod
    def delete_assessment_result(db: Session, result_id: int) -> bool:
        """删除测评结果记录"""
        db_result = db.query(AssessmentResultDB).filter(AssessmentResultDB.id == result_id).first()
        if db_result:
            db.delete(db_result)
            db.commit()
            return True
        return False

    @staticmethod
    def get_careers_by_code(db: Session, code: str) -> List[str]:
        results = db.query(HollandCareerDB).filter(HollandCareerDB.code == code).all()
        return [result.career for result in results]

    @staticmethod
    def get_all_holland_careers(db: Session) -> Dict[str, List[str]]:
        results = db.query(HollandCareerDB).all()
        careers_map = {}
        for result in results:
            if result.code not in careers_map:
                careers_map[result.code] = []
            careers_map[result.code].append(result.career)
        return careers_map