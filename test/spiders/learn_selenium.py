# https://www.cnblogs.com/zhaof/p/6953241.html
# selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。
# Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。
# selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。
#
# 用python写爬虫的时候，主要用的是selenium的Webdriver
#
# Selenium.Webdriver基本上支持了常见的所有浏览器：

# 使用之前还必须下载相关浏览器的driver
# Firefox：geckodriver.exe，下载地址：https://github.com/mozilla/geckodriver/releases
# Chrome：chromedriver.exe，下载地址：http://npm.taobao.org/mirrors/chromedriver/
# 将xxx_driver.exe文件放入你所需要执行的Python脚本的所在处，如（D:\Program Files\Python35\Scripts\）
# 参考：
# https://www.zhihu.com/question/49568096
# https://blog.csdn.net/hai4321/article/details/70339568
# https://blog.csdn.net/huilan_same/article/details/51896672



from selenium import webdriver


# 声明浏览器对象
browser = webdriver.Chrome()
# browser = webdriver.Firefox()


# # 访问页面
# browser.get('http://www.baidu.com')
# print(browser.page_source)
# browser.close()


# # 单个元素查找
# browser.get("http://www.taobao.com")
# # 这里我们通过三种不同的方式去获取响应的元素，第一种是通过id的方式，第二个中是CSS选择器，第三种是xpath选择器，结果都是相同的。
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()

# 常用的查找元素方法：
# find_element_by_name
# find_element_by_id
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector


# 下面这种方式是比较通用的一种方式：这里需要记住By模块所以需要导入
# from selenium.webdriver.common.by import By
#
# browser.get("http://www.taobao.com")
# # 这种方法和上述的方式是通用的，browser.find_element(By.ID,"q") 这里By.ID中的ID可以替换为其他几个
# input_first = browser.find_element(By.ID, "q")
# print(input_first)
# browser.close()


# # 多个元素查找
# # 其实多个元素和单个元素的区别，举个例子：find_elements,单个元素是find_element,其他使用上没什么区别，通过其中的一个例子演示：
# browser.get("http://www.taobao.com")
# lis = browser.find_elements_by_css_selector('.service-bd li')  # 这样获得就是一个列表
# print(lis)
# browser.close()


# # 元素交互操作
# import time
#
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# 运行的结果可以看出程序会自动打开Chrome浏览器并打开淘宝输入ipad,然后删除，重新输入MakBook pro，并点击搜索


# # 交互动作 | 将动作附加到动作链中串行执行
# from selenium.webdriver import ActionChains
#
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()


# # 执行JavaScript
# # 这是一个非常有用的方法，这里就可以直接调用js方法来实现一些操作，
# # 下面的例子是通过登录知乎然后通过js翻到页面底部，并弹框提示
#
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


# # 获取元素属性 | get_attribute('class')
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))


# # 获取文本值
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)


# # 获取ID，位置，标签名
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


# # Frame
# # 在很多网页中都是有Frame标签，所以我们爬取数据的时候就涉及到切入到frame中以及切出来的问题，通过下面的例子演示
# # 这里常用的是switch_to.from()和switch_to.parent_frame()
# from selenium.common.exceptions import NoSuchElementException
#
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


# 等待
# 当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常, 换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0

# # 隐式等待
# # 到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，如果超过了我们指定的时间还没有加载就会抛出异常，如果没有需要等待的时候就已经加载完毕就会立即执行
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

# # 显示等待
# # 指定一个等待条件，并且指定一个最长等待时间，会在这个时间内进行判断是否满足等待条件，如果成立就会立即返回，如果不成立，就会一直等待，直到等待你指定的最长等待时间，如果还是不满足，就会抛出异常，如果满足了就会正常返回
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# 上述的例子中的条件：EC.presence_of_element_located（）是确认元素是否已经出现了
# EC.element_to_be_clickable（）是确认元素是否是可点击的

# 常用的判断条件：
# title_is 标题是某内容
# title_contains 标题包含某内容
# presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
# visibility_of_element_located 元素可见，传入定位元组
# visibility_of 可见，传入元素对象
# presence_of_all_elements_located 所有元素加载出
# text_to_be_present_in_element 某个元素文本包含某文字
# text_to_be_present_in_element_value 某个元素值包含某文字
# frame_to_be_available_and_switch_to_it frame加载并切换
# invisibility_of_element_located 元素不可见
# element_to_be_clickable 元素可点击
# staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
# element_to_be_selected 元素可选择，传元素对象
# element_located_to_be_selected 元素可选择，传入定位元组
# element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
# element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
# alert_is_present 是否出现Alert


# # 浏览器的前进和后退
# import time
#
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()


# # cookie操作
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


# # 选项卡管理
# # 通过执行js命令实现新开选项卡window.open()
# # 不同的选项卡是存在列表里browser.window_handles
# # 通过browser.window_handles[0]就可以操作第一个选项卡
# import time
#
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')


# # 异常处理
# # 这里的异常比较复杂，官网的参考地址：
# # http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
# # 这里只进行简单的演示，查找一个不存在的元素
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
#
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()
