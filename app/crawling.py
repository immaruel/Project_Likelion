import requests
from bs4 import BeautifulSoup


def get_food(start,end=1):
    results = []
    for i in range(start, end+1):
        url = 'https://www.10000recipe.com/recipe/list.html?order=reco&page={}'.format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")
        trs = bs.select("ul.rcp_m_list2 > ul.common_sp_list_ul.ea4")
        for tr in trs:
            # 음식 사진
            photo = tr.select_one("li.common_sp_list_li > div.common_sp_thumb > a.common_sp_link > img")
            # 음식 이름 
            photo = tr.select_one

            
            results.append(name)
        
    return results

#print(get_food(1,3))