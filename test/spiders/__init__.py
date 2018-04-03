# 学习过程中的爬虫Demo - 2018-03-22

# 框架
# lxml
# BeautifulSoup
# selenium
# Scrapy

# 博客
# http://www.pythonsite.com/?cat=31
# https://github.com/kunkun1230/Python-
# https://www.cnblogs.com/kongzhagen/p/6549053.html
# https://blog.csdn.net/u011054333/article/details/70165401



# Java 爬虫框架 #################################################################
# Jsoup - https://blog.csdn.net/ccg_201216323/article/details/53576654
# 代码示例：
# public static void main(String[] args) throws Exception {
#     Jsoup.connect("http://music.163.com/playlist?id=317113395")
#             .header("Referer", "http://music.163.com/")
#             .header("Host", "music.163.com").get().select("ul[class=f-hide] a")
#             .stream().map(w-> w.text() + "-->" + w.attr("href"))
#             .forEach(System.out::println);
# }
