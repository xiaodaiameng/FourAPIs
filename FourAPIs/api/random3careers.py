# from fastapi import APIRouter, HTTPException
# from service.get_random3careers import extract_random_3_jobs, get_html_content, SAVE_PATH
# import os
# from datetime import datetime
# from deps.common_dependencies import ensure_dir_exists
#
# random3careers_router = APIRouter(prefix="/api/random3careers", tags=["careers", "random"])
#
#
# @random3careers_router.get("/")
# def get_random3careers(realtime: bool = False):
#     """
#     获取随机3个职位信息
#
#     Args:
#         realtime: 是否实时获取职位信息，默认为False（从缓存文件读取）
#
#     Returns:
#         dict: 包含随机3个职位信息的字典
#     """
#     try:
#         if realtime or not os.path.exists(SAVE_PATH):
#             # 实时获取HTML内容
#             html_content, crawler = get_html_content()
#
#             if html_content is None:
#                 raise HTTPException(status_code=500, detail="无法获取职位信息")
#         else:
#             # 从文件读取HTML内容
#             with open(SAVE_PATH, 'r', encoding='utf-8') as f:
#                 html_content = f.read()
#             # 创建一个简单的crawler对象用于统计
#             from service.get_random3careers import ZhaopinCrawler
#             crawler = ZhaopinCrawler()
#             crawler.stats['start_time'] = datetime.now()
#
#         # 提取随机3个职位
#         jobs = extract_random_3_jobs(html_content, crawler)
#
#         if not jobs:
#             raise HTTPException(status_code=404, detail="未找到任何职位信息")
#
#         # 构建响应数据
#         response = {
#             "count": len(jobs),
#             "generate_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "jobs": jobs,
#             "status": "success"
#         }
#
#         return response
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
#
#
