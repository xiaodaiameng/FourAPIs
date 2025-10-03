from config.database_config import Base, engine, get_db, init_mysql_database
from models.database_models import AssessmentResultDB, AssessmentQuestionDB, HollandCareerDB
from data.holland_questions import HOLLAND_QUESTIONS
from data.holland_careers import HOLLAND_CAREERS
import traceback


def check_tables_exist():
    try:
        from sqlalchemy import inspect
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()

        required_tables = [
            'assessment_results',
            'assessment_questions',
            'holland_careers'
        ]
        for table in required_tables:
            if table not in existing_tables:
                print(f"表 {table} 不存在")
                return False

        print("所有必需的表都已存在")
        return True
    except Exception as e:
        print(f"检查表存在性失败: {str(e)}")
        return False


def create_tables(recreate=False):
    try:
        if not recreate and check_tables_exist():
            print("表已存在，跳过创建")
            return
        if recreate:
            Base.metadata.drop_all(bind=engine)
            print("已删除现有数据库表")
        Base.metadata.create_all(bind=engine)
        print("MySQL数据库表创建成功")

        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"当前数据库中的表: {tables}")

    except Exception as e:
        print(f"创建表失败: {str(e)}")
        traceback.print_exc()


def check_questions_data_exists():
    try:
        db = next(get_db())
        count = db.query(AssessmentQuestionDB).count()
        db.close()
        if count > 0:
            print(f"数据库中已有 {count} 条测评问题数据")
            return True
        return False
    except Exception as e:
        print(f"检查问题数据失败: {str(e)}")
        return False


def init_questions_data():
    try:
        if check_questions_data_exists():
            print("测评问题数据已存在，跳过初始化")
            return

        db = next(get_db())

        questions_to_add = []
        for question in HOLLAND_QUESTIONS:
            question_db = AssessmentQuestionDB(
                id=question["id"],
                question_text=question["question"],
                options=question["options"]
            )
            questions_to_add.append(question_db)

        db.add_all(questions_to_add)
        db.commit()
        print(f"成功初始化{len(questions_to_add)}条测评问题数据")
    except Exception as e:
        print(f"初始化问题数据失败: {str(e)}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

def check_careers_data_exists():
    try:
        db = next(get_db())
        count = db.query(HollandCareerDB).count()
        db.close()
        if count > 0:
            print(f"数据库中已有 {count} 条Holland职业数据")
            return True
        return False
    except Exception as e:
        print(f"检查职业数据失败: {str(e)}")
        return False


def init_holland_careers_data():
    try:
        if check_careers_data_exists():
            print("Holland职业数据已存在，跳过初始化")
            return

        db = next(get_db())

        careers_to_add = []
        for code, careers in HOLLAND_CAREERS.items():
            for career in careers:
                career_db = HollandCareerDB(
                    code=code,
                    career=career
                )
                careers_to_add.append(career_db)

        db.add_all(careers_to_add)
        db.commit()
        print(f"成功初始化{len(careers_to_add)}条Holland职业数据")
    except Exception as e:
        print(f"初始化Holland职业数据失败: {str(e)}")
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


def init_database(recreate_tables=False):
    """初始化数据库"""
    try:
        init_mysql_database()

        create_tables(recreate=recreate_tables)

        init_questions_data()
        init_holland_careers_data()

        print("数据库初始化完成！")

    except Exception as e:
        print(f"数据库初始化失败: {str(e)}")
        traceback.print_exc()


# if __name__ == "__main__":
#     init_database()