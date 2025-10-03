
MAJOR_CATEGORIES = {
    "计算机": ["程序员", "数据分析师", "网络工程师", "系统架构师", "人工智能工程师"],
    "医学": ["医生", "护士", "药剂师", "医学研究员", "医疗技术人员"],
    "金融": ["会计师", "金融分析师", "投资顾问", "银行经理", "保险经纪人"],
    "教育": ["教师", "教育顾问", "课程设计师", "教育研究员", "心理咨询师"],
    "工程": ["工程师", "技术员", "机械师", "电工", "项目经理"],
    "艺术": ["设计师", "艺术家", "音乐家", "演员", "创意总监"],
    "管理": ["企业家", "项目经理", "行政经理", "人力资源经理", "CEO"],
    "语言": ["翻译", "作家", "编辑", "记者", "公关专员"],
    "科学": ["科学家", "研究员", "实验室技术员", "环境专家", "数学家"],
    "法律": ["律师", "法官", "法律顾问", "法律助理", "调解员"],
    "农业": ["农业技术员", "兽医", "园艺师", "农场主", "环境科学家"],
    "媒体": ["记者", "编辑", "摄影师", "视频制作人", "广告策划"],
    "建筑": ["建筑师", "土木工程师", "室内设计师", "城市规划师", "测量师"],
    "服务": ["社会工作者", "心理咨询师", "公关专员", "客服经理", "导游"],
}

# 具体专业名称到专业类别的映射
MAJOR_TO_CATEGORY = {
    "计算机科学": "计算机",
    "软件工程": "计算机",
    "数据科学": "计算机",
    "人工智能": "计算机",
    "电子工程": "工程",
    "机械工程": "工程",
    "土木工程": "工程",
    "临床医学": "医学",
    "护理学": "医学",
    "药学": "医学",
    "金融学": "金融",
    "会计学": "金融",
    "财务管理": "金融",
    "教育学": "教育",
    "心理学": "教育",
    "汉语言文学": "语言",
    "英语": "语言",
    "法学": "法律",
    "工商管理": "管理",
    "市场营销": "管理",
    "人力资源管理": "管理",
    "艺术设计": "艺术",
    "音乐表演": "艺术",
    "广播电视编导": "媒体",
    "新闻学": "媒体",
    "数学": "科学",
    "物理": "科学",
    "化学": "科学",
    "生物科学": "科学",
    "建筑学": "建筑",
    "城乡规划": "建筑",
    "社会工作": "服务",
    "旅游管理": "服务",
    "农学": "农业",
    "动物医学": "农业"
}

# 职业匹配
CAREER_DETAILS = {
    "程序员": {"description": "负责软件开发和维护", "holland_codes": {"I": 90, "R": 70, "C": 60}},
    "数据分析师": {"description": "分析和解读数据以支持决策", "holland_codes": {"I": 95, "C": 85, "R": 60}},
    "网络工程师": {"description": "设计和维护计算机网络系统", "holland_codes": {"R": 85, "I": 80, "C": 75}},
    "系统架构师": {"description": "设计复杂的计算机系统架构", "holland_codes": {"I": 95, "R": 80, "E": 70}},
    "人工智能工程师": {"description": "开发智能系统和算法", "holland_codes": {"I": 100, "R": 85, "A": 65}},
    "医生": {"description": "诊断和治疗疾病", "holland_codes": {"I": 90, "S": 95, "E": 70}},
    "护士": {"description": "照顾病人并协助医生", "holland_codes": {"S": 100, "C": 80, "I": 75}},
    "药剂师": {"description": "调配和提供药物咨询", "holland_codes": {"I": 90, "C": 95, "S": 80}},
    "医学研究员": {"description": "进行医学研究和实验", "holland_codes": {"I": 100, "R": 85, "C": 80}},
    "医疗技术人员": {"description": "操作医疗设备和进行检测", "holland_codes": {"R": 90, "C": 85, "I": 80}},
    "会计师": {"description": "处理财务记录和报表", "holland_codes": {"C": 100, "I": 80, "E": 65}},
    "金融分析师": {"description": "分析金融市场和投资机会", "holland_codes": {"I": 95, "E": 90, "C": 85}},
    "投资顾问": {"description": "提供投资建议和管理投资组合", "holland_codes": {"E": 95, "I": 90, "S": 75}},
    "银行经理": {"description": "管理银行分支机构和业务", "holland_codes": {"E": 100, "S": 90, "C": 85}},
    "保险经纪人": {"description": "销售保险产品和提供咨询", "holland_codes": {"E": 95, "S": 90, "C": 80}},
    "教师": {"description": "教育学生和传授知识", "holland_codes": {"S": 100, "A": 85, "I": 80}},
    "教育顾问": {"description": "提供教育规划和咨询服务", "holland_codes": {"S": 95, "E": 85, "I": 80}},
    "课程设计师": {"description": "设计教学课程和材料", "holland_codes": {"A": 90, "S": 85, "I": 80}},
    "教育研究员": {"description": "研究教育理论和实践", "holland_codes": {"I": 95, "S": 85, "A": 75}},
    "心理咨询师": {"description": "提供心理评估和咨询服务", "holland_codes": {"S": 100, "I": 90, "A": 80}},
    "工程师": {"description": "设计和开发各种工程解决方案", "holland_codes": {"R": 95, "I": 90, "C": 85}},
    "技术员": {"description": "协助工程师进行技术工作", "holland_codes": {"R": 100, "C": 85, "I": 80}},
    "机械师": {"description": "修理和维护机械设备", "holland_codes": {"R": 100, "C": 80, "I": 75}},
    "电工": {"description": "安装和维修电气系统", "holland_codes": {"R": 100, "C": 85, "I": 70}},
    "项目经理": {"description": "规划和管理项目的执行", "holland_codes": {"E": 95, "C": 90, "S": 85}},
    "设计师": {"description": "创建视觉设计和产品", "holland_codes": {"A": 100, "I": 85, "R": 75}},
    "艺术家": {"description": "创作艺术作品表达创意", "holland_codes": {"A": 100, "I": 80, "S": 65}},
    "音乐家": {"description": "创作和表演音乐", "holland_codes": {"A": 100, "S": 85, "E": 70}},
    "演员": {"description": "在舞台或屏幕上表演", "holland_codes": {"A": 100, "S": 90, "E": 85}},
    "创意总监": {"description": "监督创意项目和团队", "holland_codes": {"A": 95, "E": 95, "S": 85}},
    "企业家": {"description": "创办和管理企业", "holland_codes": {"E": 100, "I": 90, "S": 85}},
    "行政经理": {"description": "管理组织的行政事务", "holland_codes": {"C": 95, "E": 90, "S": 85}},
    "人力资源经理": {"description": "管理组织的人力资源", "holland_codes": {"S": 100, "E": 90, "C": 85}},
    "CEO": {"description": "领导和管理整个组织", "holland_codes": {"E": 100, "S": 95, "I": 90}},
    "翻译": {"description": "在不同语言之间进行翻译", "holland_codes": {"C": 90, "I": 85, "S": 80}},
    "作家": {"description": "创作文学作品", "holland_codes": {"A": 100, "I": 95, "C": 75}},
    "编辑": {"description": "编辑和校对文本", "holland_codes": {"C": 95, "A": 90, "I": 85}},
    "记者": {"description": "收集和报道新闻", "holland_codes": {"S": 95, "E": 90, "A": 85}},
    "公关专员": {"description": "管理组织的公共关系", "holland_codes": {"S": 100, "E": 95, "A": 85}},
    "律师": {"description": "提供法律咨询和代理诉讼", "holland_codes": {"E": 95, "I": 95, "C": 90}},
    "法官": {"description": "审理案件并做出判决", "holland_codes": {"E": 90, "I": 95, "C": 95}},
    "法律顾问": {"description": "提供专业法律建议", "holland_codes": {"I": 95, "C": 95, "E": 85}},
    "法律助理": {"description": "协助律师处理法律事务", "holland_codes": {"C": 100, "I": 90, "E": 75}},
    "调解员": {"description": "协助解决争端", "holland_codes": {"S": 100, "E": 90, "I": 85}},
    "科学家": {"description": "进行科学研究和实验", "holland_codes": {"I": 100, "R": 90, "C": 85}},
    "研究员": {"description": "深入研究特定领域", "holland_codes": {"I": 100, "C": 90, "R": 85}},
    "实验室技术员": {"description": "在实验室进行技术工作", "holland_codes": {"R": 95, "C": 95, "I": 90}},
    "环境专家": {"description": "研究和解决环境问题", "holland_codes": {"I": 95, "R": 90, "S": 85}},
    "数学家": {"description": "研究数学理论和应用", "holland_codes": {"I": 100, "C": 95, "R": 80}},
    "建筑师": {"description": "设计建筑物和结构", "holland_codes": {"A": 95, "I": 90, "R": 85}},
    "土木工程师": {"description": "设计和建造基础设施", "holland_codes": {"R": 95, "I": 90, "C": 85}},
    "室内设计师": {"description": "设计室内空间", "holland_codes": {"A": 100, "R": 85, "I": 80}},
    "城市规划师": {"description": "规划城市发展", "holland_codes": {"I": 95, "E": 90, "S": 85}},
    "测量师": {"description": "测量土地和空间", "holland_codes": {"R": 95, "C": 95, "I": 85}},
    "社会工作者": {"description": "帮助有需要的人群", "holland_codes": {"S": 100, "I": 90, "A": 85}},
    "客服经理": {"description": "管理客户服务团队", "holland_codes": {"S": 95, "E": 90, "C": 85}},
    "导游": {"description": "带领和解说旅游行程", "holland_codes": {"S": 100, "E": 90, "A": 80}},
    "农业技术员": {"description": "提供农业技术支持", "holland_codes": {"R": 95, "I": 90, "C": 85}},
    "兽医": {"description": "诊断和治疗动物疾病", "holland_codes": {"R": 90, "I": 95, "S": 90}},
    "园艺师": {"description": "栽培和照料植物", "holland_codes": {"R": 100, "A": 90, "I": 80}},
    "农场主": {"description": "经营农场和农业生产", "holland_codes": {"R": 95, "E": 95, "I": 85}},
    "环境科学家": {"description": "研究环境问题和解决方案", "holland_codes": {"I": 95, "R": 90, "S": 85}},
    "摄影师": {"description": "拍摄照片记录影像", "holland_codes": {"A": 100, "R": 85, "S": 80}},
    "视频制作人": {"description": "制作视频内容", "holland_codes": {"A": 95, "E": 90, "R": 85}},
    "广告策划": {"description": "策划和执行广告活动", "holland_codes": {"E": 95, "A": 95, "S": 90}}
}

# 获取专业所属的类别
def get_major_category(major_name):
    # 精确匹配
    if major_name in MAJOR_TO_CATEGORY:
        return MAJOR_TO_CATEGORY[major_name]
    # 模糊匹配
    for keyword, category in MAJOR_TO_CATEGORY.items():
        if keyword in major_name:
            return category
    # 如果没有匹配，返回默认类别
    return "其他"

# 获取与专业相关的职业列表
def get_major_related_careers(major_name):
    """获取与指定专业相关的职业列表"""
    category = get_major_category(major_name)
    return MAJOR_CATEGORIES.get(category, []) + MAJOR_CATEGORIES.get("其他", [])

# 计算
def calculate_career_match_score(career_name, user_traits):
    if career_name not in CAREER_DETAILS:
        return 0
    career_details = CAREER_DETAILS[career_name]
    score = 0
    for trait, user_score in user_traits.items():
        if trait in career_details["holland_codes"]:
            # 得分越高的特质，权重越大
            score += career_details["holland_codes"][trait] * user_score
    return score

def get_career_description(career_name, user_major, user_traits):
    if career_name not in CAREER_DETAILS:
        return f"有关职业'{career_name}'的信息暂未收录。"
    base_desc = CAREER_DETAILS[career_name]["description"]
    category = get_major_category(user_major)
    match_traits = []
    for trait, _ in sorted(user_traits.items(), key=lambda x: x[1], reverse=True)[:2]:
        match_traits.append(trait)
    
    if category in MAJOR_CATEGORIES:
        if career_name in MAJOR_CATEGORIES[category]:
            relevance = "高度相关"
        else:
            relevance = "潜在相关"
    else:
        relevance = "可能相关"
    return f"{base_desc}。这个职业与您的专业{user_major}{relevance}，适合具有{','.join(match_traits)}特质的人。"