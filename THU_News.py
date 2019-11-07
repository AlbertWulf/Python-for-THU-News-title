import requests
from bs4 import BeautifulSoup
import bs4
import csv
def README():
    print("Make sure that u have install package below:")
    print("requests,pandas,bs4,csv")
    print("Functions available in this package:")
    print("get_Hot(page_index)")
    

def get_Hot(page_index):

    print("Loading data...")
    url = "http://news.tsinghua.edu.cn/publish/thunews/9648/index_10.html#"
    headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Host" : "news.tsinghua.edu.cn",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language" : "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
    }
    rows = []
    k = 0
    for j in range(1,page_index):
        nn = str(j)
        url = "http://news.tsinghua.edu.cn/publish/thunews/9648/index_"+ nn + ".html#"
        response = requests.get(url = url)
        page_text = response.text.encode("latin1").decode("utf-8")
        soup = BeautifulSoup(page_text,"html.parser")
        name_list = soup.find_all("li",{"class":"clearfix"})
        head = ["No","Title"]
        for i in name_list:
            s = i.find("a",{"class":"jiequ"}).string
            dic = {"No":k,"title":s.string}
            k = k+1
            rows.append(dic)
    print("Write CSV file...")
    with open("thu.csv","a",newline="") as f:
        f_csv = csv.DictWriter(f,head)
        f_csv.writeheader()
        f_csv.writerows(rows)
        print("Finished !")
