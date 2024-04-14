from pprint import pprint
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_cookie():
    driver = webdriver.Edge()
    driver.get('https://passport.bilibili.com/login')
    # 在此处手动登录进入你的 Bilibili 账号
    input("登录完成后，请按 Enter 键继续...")
    cookies = driver.get_cookies()
    pprint(cookies)
    driver.quit()
   
   
cookies_for_bilibili = [{'domain': '.bilibili.com',
  'expiry': 1740920769,
  'httpOnly': False,
  'name': 'browser_resolution',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '988-667'},
 {'domain': '.bilibili.com',
  'expiry': 1740920769,
  'httpOnly': False,
  'name': 'home_feed_column',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '4'},
 {'domain': '.bilibili.com',
  'expiry': 1740920769,
  'httpOnly': False,
  'name': 'header_theme_version',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': 'CLOSE'},
 {'domain': '.bilibili.com',
  'expiry': 1740920769,
  'httpOnly': False,
  'name': 'enable_web_push',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': 'DISABLE'},
 {'domain': 'www.bilibili.com',
  'httpOnly': False,
  'name': 'bmg_src_def_domain',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': 'i0.hdslb.com'},
 {'domain': 'www.bilibili.com',
  'httpOnly': False,
  'name': 'bmg_af_switch',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '1'},
 {'domain': '.bilibili.com',
  'expiry': 1740920764,
  'httpOnly': False,
  'name': '_uuid',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '191310873-CEAC-E855-AB104-EC8C17B2245264045infoc'},
 {'domain': '.bilibili.com',
  'expiry': 1740920769,
  'httpOnly': False,
  'name': 'FEED_LIVE_VERSION',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': 'V8'},
 {'domain': '.bilibili.com',
  'expiry': 1724936760,
  'httpOnly': False,
  'name': 'sid',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '7ax3hd69'},
 {'domain': '.bilibili.com',
  'expiry': 1740920711,
  'httpOnly': False,
  'name': 'b_nut',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '1709384712'},
 {'domain': '.bilibili.com',
  'expiry': 1724936760,
  'httpOnly': False,
  'name': 'DedeUserID__ckMd5',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '4ee9d1d5451f2c32'},
 {'domain': '.bilibili.com',
  'httpOnly': False,
  'name': 'b_lsid',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '85D62B65_18DFF458A80'},
 {'domain': '.bilibili.com',
  'expiry': 1743944764,
  'httpOnly': False,
  'name': 'buvid_fp',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '47fe91d7c77a4f143795cbcf55a3bf56'},
 {'domain': '.bilibili.com',
  'expiry': 1724936760,
  'httpOnly': False,
  'name': 'bili_jct',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '93313f935d02f1bdacd147fbca92c6eb'},
 {'domain': '.bilibili.com',
  'expiry': 1709643913,
  'httpOnly': False,
  'name': 'bili_ticket',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk2NDM5MTMsImlhdCI6MTcwOTM4NDY1MywicGx0IjotMX0.qB1tZ7B_ouPdTLDwsaJYXlUjLUVzuUbT0lcTv8610N4'},
 {'domain': '.bilibili.com',
  'expiry': 1743944711,
  'httpOnly': False,
  'name': 'buvid3',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '55C56993-0950-E2C6-5EF5-122BC63640F112295infoc'},
 {'domain': '.bilibili.com',
  'expiry': 1743944713,
  'httpOnly': False,
  'name': 'buvid4',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '1D13C7D9-56A9-310F-BE93-535F062F5B5C13601-024030213-oFp9CWbaLplJb2TOmlqB1RA8QnmFbTa8x0tUaipzT9Gm0mLodKF3nfU1jeKnBoXj'},
 {'domain': '.bilibili.com',
  'expiry': 1709643913,
  'httpOnly': False,
  'name': 'bili_ticket_expires',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '1709643853'},
 {'domain': '.bilibili.com',
  'expiry': 1724936760,
  'httpOnly': False,
  'name': 'DedeUserID',
  'path': '/',
  'sameSite': 'Lax',
  'secure': False,
  'value': '1221404996'},
 {'domain': '.bilibili.com',
  'expiry': 1724936760,
  'httpOnly': True,
  'name': 'SESSDATA',
  'path': '/',
  'sameSite': 'Lax',
  'secure': True,
  'value': '7454b3e8%2C1724936761%2C81743%2A32CjBq7it3Ut5pt-HbiFdykaJbRVS9oJkwMoME3OxXPrRZDcsce_iPRnnI9Itrw_ZvpdkSVjZtOXhMWFV2Mmo0WU9QZE5SNWZySWJTM2hkVHJyamFxRTFJejZreGFjT2praFFhamk3Wmt1NkgwM012N0JTNUZRMTRHdFFJNVA2N1VFTVlIdlJRcU93IIEC'}]

def open_video():
    global driver
    driver = webdriver.Edge()
    driver.maximize_window()
    #url = 'https://www.bilibili.com'
    url = 'https://www.bilibili.com/video/BV1Jm411D7ht/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=8063562aea380939b2d9ca0e1126afbe'
    driver.get(url)
    for _ in cookies_for_bilibili:
        driver.add_cookie(_)
    driver.refresh()
    print("bilibili已被打开！")

def search():
    print("请输入内容")
    text=input()
    element1 = driver.find_element(By.CSS_SELECTOR, '#nav-searchform > div.nav-search-content > input')
    element2 = driver.find_element(By.CSS_SELECTOR, '#nav-searchform > div.nav-search-content > input')
    element3 = driver.find_element(By.CSS_SELECTOR, '#nav-searchform > div.nav-search-btn')
    element1.send_keys(text)
    element3.click()
    print(f"已为您搜索有关{text}的相关内容！")

def like():
    element4 = driver.find_element(By.CSS_SELECTOR,'#arc_toolbar_report > div.video-toolbar-left > div.video-toolbar-left-main > div:nth-child(1) > div')
    element4.click()
    global count1
    count1 += 1
    if(count1 % 2!= 0):
        print("点赞成功！")
    else:
        print("您已取消点赞！")

def play_or_stop():
    element5 = driver.find_element(By.CSS_SELECTOR,'#bilibili-player > div > div > div.bpx-player-primary-area > div.bpx-player-video-area > div.bpx-player-control-wrap > div.bpx-player-control-entity > div.bpx-player-control-bottom > div.bpx-player-control-bottom-left > div.bpx-player-ctrl-btn.bpx-player-ctrl-play > div > span')
    element5.click()
    global count2
    count2 += 1
    if(count2 % 2!= 0):
        print("您已暂停视频")
    else:
        print("视频已继续播放")

def out():
    print("please waiting for a moment")
    driver.quit()
    print(f"本次运行共执行{count}条您的指令")
    print("期待您的下次使用！")
    
a=0
driver = None
count = 0
count1 = 0
count2 = 0
while a>=0:
    count += 1
    print("----------------------------------------------")
    print("1.打开 2.搜索 3.点赞 4.暂停 5.关闭")
    try:
        a = int(input("请输入指令代号："))
    except ValueError as e:
        print("请输入数字代号，而不是其他字符命令")
        continue
        
    if a==1 :
        open_video()
    elif (a== 2):
        search()
    elif (a== 3):
        like()
    elif (a == 4):
        play_or_stop()
    elif(a == 5):
        out()
        break
    else:
        print("请输入范围内的指令代号")