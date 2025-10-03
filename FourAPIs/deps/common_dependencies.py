from fastapi import Depends, HTTPException
from typing import Dict
import os

# 简化的身份验证依赖 - 始终返回匿名用户
def get_current_user():
    return {
        "username": "anonymous",
        "role": "guest"
    }

# 简化的获取已认证用户ID依赖
def get_authenticated_user_id(current_user: Dict = Depends(get_current_user)):
    return current_user["username"]

# 确保目录存在的工具函数
def ensure_dir_exists(dir_path: str) -> bool:
    """
    确保指定的目录存在，如果不存在则创建
    
    Args:
        dir_path: 目录路径
        
    Returns:
        bool: 是否成功（或目录已存在）
    """
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        return True
    except Exception as e:
        print(f"创建目录失败: {str(e)}")
        return False