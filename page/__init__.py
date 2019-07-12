
"""
以下为登录页面配置数据
"""
from selenium.webdriver.common.by import By

# 输入手机号信息
input_phone = By.ID, "com.vcooline.aike:id/etxt_username"
# 输入密码
input_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
# 点击登录信息
click_btn = By.ID, "com.vcooline.aike:id/btn_login"
