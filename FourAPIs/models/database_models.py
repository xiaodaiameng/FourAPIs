from sqlalchemy import Column, Integer, String, Text, JSON
from config.database_config import Base

class AssessmentResultDB(Base):
    __tablename__ = "assessment_results"
    
    id = Column(Integer, primary_key=True, index=True)
    result = Column(String(2), nullable=False)  # 只存储两个字母


class AssessmentQuestionDB(Base):
    __tablename__ = "assessment_questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    options = Column(JSON)


class HollandCareerDB(Base):
    __tablename__ = "holland_careers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(1), nullable=False, index=True)
    career = Column(String(50), nullable=False)