# 霍兰德职业兴趣测评系统 - 数据库配置指南

## 数据库要求

本项目使用MySQL数据库存储测评相关数据。请确保您已安装MySQL服务器，并具有创建数据库和表的权限。

## 配置步骤

### 1. 安装必要的依赖

首先，请确保安装了项目所需的所有依赖：

```bash
pip install -r requirements.txt
```

### 2. 修改数据库配置

编辑`config/settings.py`文件，根据您的MySQL服务器配置修改以下参数：

```python
# 数据库配置参数
DATABASE_CONFIG = {
    "username": "root",  # 您的MySQL用户名
    "password": "password",  # 您的MySQL密码
    "host": "localhost",  # MySQL服务器地址
    "port": 3306,  # MySQL端口号
    "database": "assessment_db"  # 数据库名称
}
```

### 3. 创建数据库

在运行项目之前，您需要创建MySQL数据库。可以使用以下SQL命令：

```sql
CREATE DATABASE assessment_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

请确保您的MySQL用户具有创建数据库和表的权限。

### 4. 运行项目

当您运行项目时，系统会自动创建必要的表并初始化测评问题数据：

```bash
uvicorn main:app --reload
```

## 数据库结构

系统创建了两个表：

### 1. assessment_results（测评结果表）

- `id`: 主键，自动递增
- `result`: 存储测评结果的两个字母（例如"RI"、"AE"等）

### 2. assessment_questions（测评问题表）

- `id`: 主键，问题ID
- `question_text`: 问题文本

## 注意事项

1. 如果您遇到数据库连接问题，请检查MySQL服务器是否正在运行，以及配置的用户名和密码是否正确。

2. 如果初始化过程中出现问题，请确保您的MySQL用户具有足够的权限来创建表和插入数据。

3. 系统启动时会自动检查数据库表是否存在，如果不存在则会创建表并初始化问题数据。

4. 测评结果会在用户提交测评后自动保存到数据库中。

5. 系统不会创建用户表，因为这部分功能由其他同学负责。