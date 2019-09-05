from bs4 import BeautifulSoup
import requests
import time
import datetime

news_num = 0
date_info = time.strftime("%m-%d", time.localtime())

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    }

iotworld_url = "http://www.iotworld.com.cn/"
cnblogs_url = "https://news.cnblogs.com/"
eepw_url = "http://www.eepw.com.cn/news"
aliyun_url = "https://yq.aliyun.com"
people_url = "http://scitech.people.com.cn/GB/1056/index1.html"
people_dynamic_url = "http://scitech.people.com.cn/GB/1057/index.html"
zanbtc_url = "https://www.zanbtc.com/forum.php?mod=forumdisplay&fid=2&filter=lastpost&orderby=lastpost"
jutuilian_url = "https://www.jutuilian.com/news/"
baidu_url = "http://news.baidu.com/tech"
sina_url = "https://tech.sina.com.cn/"
sohu_url = "http://it.sohu.com/?spm=smpc.ch30.header.9.1561085132478R6VrYV9"

class FaceFutureNews:

    @staticmethod
    def compare_span_date(str, date):
        span_info = str.find_all("span")
        for item in span_info:
            try:
                news_date = item.get("title")
                if (date in news_date) or (date.strip("0") in news_date):
                    return True
            except:
                pass
            if (date in item.text) or (date.strip("0") in item.text):
                return True
            else:
                continue
        return False

    @staticmethod
    def compare_em_date(str, date):
        em_info = str.find_all("em")
        for item in em_info:
            if date in item.text:
                return True
            else:
                continue
        return False

    # 物联网世界
    @staticmethod
    def iotworld_get_news():
        url = iotworld_url
        print("%s: 物联网世界新闻：\n"%date_info)
        get_response = requests.get(url,headers=headers,params=None)
        soup = BeautifulSoup(get_response.content,"html.parser")
        num = 0
        fp = open("news_info.txt","a+")
        for item in soup.find_all("a"):
            res = item.find("span")
            if res:
                date_text = res.text
                if date_info in date_text:
                    num += 1
                    # print("************************************************************************************************************")
                    fp.write("NEWS_%s：%s \n链接：%s\n"% (str(num),item.get('title'), item.get('href')))
                    print("NEWS_%s：%s \n链接：%s\n"% (str(num),item.get('title'), item.get('href')))
                    # res = requests.get(item.get("href"))
                    # res_soup = BeautifulSoup(res.content,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
        if num==0:
            print("今日暂无新闻")

    # 博客园
    def cnblogs_get_news(self):
        print("%s: 博客园新闻：\n" % date_info)
        befor_url = "https://news.cnblogs.com"
        url = cnblogs_url
        get_response = requests.get(url,headers=headers,params=None)
        soup = BeautifulSoup(get_response.content,"html.parser")
        if soup.find_all("div"):
            num = 0
            for item in soup.find_all(name="div", attrs={"class": "content"}):
                if self.compare_span_date(item, date_info):
                    num += 1
                    news = item.find("a")
                    # print("************************************************************************************************************")
                    print("NEWS_%s：%s \n链接:%s\n"%(str(num), news.text, befor_url+news.get("href")))
                    # res = requests.get(befor_url+news.get("href"))
                    # res_soup = BeautifulSoup(res.text,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
            if num==0:
                print("今日暂无新闻")

    # EEPW杂志
    def eepw_get_news(self):
        print("%s: EEPW新闻：\n" % date_info)
        url = eepw_url
        get_response = requests.get(url,headers=headers,params=None)
        soup = BeautifulSoup(get_response.content,"html.parser")
        if soup.find_all("div"):
            num = 0
            for item in soup.find_all(name="li", attrs={"class":"newstype2 clear"}):
                # print("************************************************************************************************************")
                # print(item)
                if self.compare_span_date(item, date_info):
                    num += 1
                    news = item.find("a")
                    print("NEWS_%s：%s \n链接:%s\n"%(str(num),news.get("title"),news.get("href")))
                    # res = requests.get(befor_url+news.get("href"))
                    # res_soup = BeautifulSoup(res.text,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
            if num==0:
                print("今日暂无新闻")

    # 阿里云社区
    def aliyun_get_news(self):
        print("%s: 阿里云社区新闻：\n" % date_info)
        url = aliyun_url
        befor_url = "https://yq.aliyun.com"
        get_response = requests.get(url,headers=headers,params=None)
        soup = BeautifulSoup(get_response.content,"html.parser")
        if soup.find_all("div"):
            num = 0
            for item in soup.find_all(name="div", attrs={"class":"item-box"}):
                # print("************************************************************************************************************")
                # print(item)
                if self.compare_span_date(item, date_info):
                    num += 1
                    news = item.find("a")
                    title = item.find("h3").text.strip().split("    ")
                    t_len = len(title)
                    print("NEWS_%s：%s \n链接:%s\n"%(str(num),title[t_len-1] , befor_url+news.get("href")))
                    # res = requests.get(befor_url+news.get("href"))
                    # res_soup = BeautifulSoup(res.text,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
            if num==0:
                print("今日暂无新闻")

    # 人民网科学界
    def people_get_news(self):
        print("%s: 人民网科学界新闻：\n" % date_info)
        url = people_url
        befor_url = "http://scitech.people.com.cn"
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        if soup.find_all("div"):
            num = 0
            for item in soup.find_all(name="ul", attrs={"class": "list_16 mt10"}):
                # print("************************************************************************************************************")
                # print(item)
                if self.compare_em_date(item, date_info):
                    num += 1
                    news = item.find("a")
                    print("NEWS_%s：%s \n链接:%s\n" % (str(num), news.text, befor_url + news.get("href")))
                    # res = requests.get(befor_url+news.get("href"))
                    # res_soup = BeautifulSoup(res.text,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
            if num==0:
                print("今日暂无新闻")

    # 人民网科技动态新闻
    def people_get_dynamic_news(self):
        print("%s: 人民网科技动态新闻：\n" % date_info)
        url = people_dynamic_url
        befor_url = "http://scitech.people.com.cn"
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        if soup.find_all("div"):
            num = 0
            for item in soup.find_all(name="li"):
                # print("************************************************************************************************************")
                # print(item)
                if self.compare_em_date(item, date_info):
                    num += 1
                    news = item.find("a")
                    print("NEWS_%s：%s \n链接:%s\n" % (str(num), news.text, befor_url + news.get("href")))
                    # res = requests.get(befor_url+news.get("href"))
                    # res_soup = BeautifulSoup(res.text,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
            if num == 0:
                print("今日暂无新闻")

    # 比特币—赞比社区新闻
    def zanbtc_get_news(self):
        print("%s: 赞比社区比特币新闻：\n" % date_info)
        url = zanbtc_url
        befor_url = "https://www.zanbtc.com/"
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        if soup.find_all("tbody"):
            num = 0
            for item in soup.find_all(name="div",attrs={"style":"padding-left: 60px;"}):
                # print("************************************************************************************************************")
                # print(item)
                if self.compare_span_date(item, date_info):
                    num += 1
                    news = item.find(name="a",attrs={"class":"s"})
                    print("NEWS_%s：%s \n链接:%s\n" % (str(num), news.text, befor_url + news.get("href").strip("amp;")))
                    # res = requests.get(befor_url+news.get("href"))
                    # res_soup = BeautifulSoup(res.text,"html.parser")
                    # for ele in res_soup.find_all("p"):
                    #     print(ele.text.strip())
            if num==0:
                print("今日暂无新闻")

    # 比特币—巨推链社区新闻
    def jutuilian_get_news(self):
        print("%s: 巨推链社区新闻：\n" % date_info)
        url = jutuilian_url
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        if soup.find_all("div"):
            num = 0
            for item in soup.find_all(name="div", attrs={"class": "recommend_article_list_content"}):
                # print("************************************************************************************************************")
                # print(item)
                try:
                    if self.compare_span_date(item, date_info):
                        num += 1
                        news = item.find(name="a")
                        print("NEWS_%s：%s \n链接:%s\n" % (str(num), news.text, news.get("href")))
                        # res = requests.get(befor_url+news.get("href"))
                        # res_soup = BeautifulSoup(res.text,"html.parser")
                        # for ele in res_soup.find_all("p"):
                        #     print(ele.text.strip())
                except:
                    pass

            if num == 0:
                print("今日暂无新闻")

    # 百度科技新闻
    def baidu_get_news(self):
        print("%s: 百度科技新闻：\n" % date_info)
        url = baidu_url
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        news_arry = []
        news_arry.append(soup.find_all("div", id="internet_news"))
        news_arry.append(soup.find_all("div",id="mod_internet"))
        news_arry.append(soup.find_all("div",attrs={"class":"middle-focus-news"}))
        news_arry.append(soup.find_all("div", id="kj_news"))
        num = 0
        temp_arry = []
        for i in range(0,len(news_arry)):
            for item in news_arry[i]:
                for ele in item.find_all("li"):

                    a_info = ele.find("a")
                    a_url = a_info.get("href")
                    a_text = a_info.text
                    # print(a_text, a_url)
                    get_a_response = requests.get(a_url, headers=headers, params=None)
                    a_soup = BeautifulSoup(get_a_response.content, "html.parser")
                    news_date = a_soup.find("span", attrs={"class": "date"})
                    try:
                        # print(news_date.text)
                        if (date_info in news_date.text) or (date_info.strip("0") in news_date.text):
                            match_time = 0
                            for i in range(0,len(temp_arry)):
                                if temp_arry[i] in a_url:
                                    match_time += 1
                            if match_time==0:
                                temp_arry.append(a_url)
                                num += 1
                                print("NEWS_%s：%s \n链接:%s\n" %(num,a_text, a_url))
                    except:
                        pass

        if num == 0:
            print("今日暂无新闻")

    # 新浪科技新闻
    def sina_get_news(self):
        print("%s: 新浪科技新闻：\n" % date_info)
        url = sina_url
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        temp_arry = []
        num = 0
        for item in soup.find_all("ul",attrs={"class":"rank-con"}):
            for ele in item.find_all("li"):
                a_info = ele.find("a")
                a_url = a_info.get("href")
                a_text = a_info.text
                # print(a_text, a_url)
                get_a_response = requests.get(a_url, headers=headers, params=None)
                a_soup = BeautifulSoup(get_a_response.content, "html.parser")
                news_date = a_soup.find("meta", attrs={"property":"article:published_time"})
                # print(news_date.text)
                try:
                    if (date_info in news_date.get("content")) or (date_info.strip("0") in news_date.get("content")):
                        match_time = 0
                        for i in range(0, len(temp_arry)):
                            if temp_arry[i] in a_url:
                                match_time += 1
                        if match_time == 0:
                            temp_arry.append(a_url)
                            num += 1
                            print("NEWS_%s：%s \n链接:%s\n" % (num, a_text, a_url))
                except:
                    pass

        if num == 0:
            print("今日暂无新闻")

    # 搜狐科技新闻
    def sohu_get_news(self):
        print("%s: 搜狐科技新闻：\n" % date_info)
        url = sohu_url
        get_response = requests.get(url, headers=headers, params=None)
        soup = BeautifulSoup(get_response.content, "html.parser")
        temp_arry = []
        num = 0
        for item in soup.find_all("div"):
            # print("***********************************************")
            # print(item)
            for ele in item.find_all("li"):
                # print(ele)
                a_info = ele.find_all("span",attrs={"class":"title-link"})
                for var in a_info:
                    a_url = var.get("href")
                    if "http" not in a_url:
                        a_url = "http:" + a_url
                    a_text = var.text
                    # print(a_text, a_url)
                    get_a_response = requests.get(a_url, headers=headers, params=None)
                    a_soup = BeautifulSoup(get_a_response.content, "html.parser")
                    news_date = a_soup.find("meta", attrs={"itemprop": "datePublished"})
                    # print(news_date.text)
                    try:
                        if (date_info in news_date.get("content")) or (date_info.strip("0") in news_date.get("content")):
                            match_time = 0
                            for i in range(0, len(temp_arry)):
                                if temp_arry[i] in a_url:
                                    match_time += 1
                            if match_time == 0:
                                temp_arry.append(a_url)
                                num += 1
                                print("NEWS_%s：%s \n链接:%s\n" % (num, a_text, a_url))
                    except:
                        pass

        if num == 0:
            print("今日暂无新闻")


    def get_all_news(self):
        print("技术社区新闻：")
        # 阿里云社区
        self.aliyun_get_news()
        print("\n*************************************")
        # 博客园新闻
        self.cnblogs_get_news()
        print("\n*************************************")
        # 物联网世界新闻
        self.iotworld_get_news()
        print("\n*************************************")
        # EEPW新闻
        self.eepw_get_news()
        print("\n*************************************")
        # 赞比社区新闻
        self.zanbtc_get_news()
        print("\n*************************************")
        # 巨推链社区新闻
        self.jutuilian_get_news()


        print("国家官网科技新闻：")
        print("\n*************************************")
        # 人民网科学界新闻
        self.people_get_news()
        print("\n*************************************")
        # 人民网科技动态新闻
        self.people_get_dynamic_news()


        print("各大门户网站科技新闻：")
        print("\n*************************************")
        # 百度科技新闻
        self.baidu_get_news()
        print("\n*************************************")
        # 新浪科技新闻
        self.sina_get_news()
        print("\n*************************************")
        # 搜狐科技新闻
        self.sohu_get_news()

if __name__ == "__main__":
    ffn = FaceFutureNews()
    ffn.get_all_news()