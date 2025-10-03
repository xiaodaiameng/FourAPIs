# import os
# import json
#
# import playwright
# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup
#
# # config
# TARGET_URL = "https://www.zhaopin.com/sou/jl489/p2?el=4&sl=15001,25000&et=2"
# COOKIE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
# COOKIE_PATH = os.path.join(COOKIE_DIR, "Cookies_zhaopin.txt")
# EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
#
# # 提前创建目录（避免保存时路径不存在）
# os.makedirs(COOKIE_DIR, exist_ok=True)
#
# with playwright as p:
#     browser = p.chromium.launch(headless=False, slow_mo=300, executable_path=EDGE_PATH,
#                                 args=["--disable-popup-blocking"])
#     page = browser.new_page()
#     page.set_viewport_size({"width": 1200, "height": 800})  # 放大窗口，避免页面加载异常
#     try:
#         #     page.goto(TARGET_URL, wait_until="domcontentloaded")
#         #     page.goto(TARGET_URL, wait_until="networkidle")# 更久
#
#         # 后续解析页面逻辑
#         page_source = page.content()
#         soup = BeautifulSoup(page_source, 'html.parser')
#         print("页面解析成功")
#
#     except Exception as e:
#         print(f"错误：{e}")
#     finally:
#         browser.close()  # 确保浏览器关闭