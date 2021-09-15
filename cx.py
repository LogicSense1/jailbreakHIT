import requests
from calendar import Calendar


cookie = '' # your cookie here

headers = {"accept": "application/json, text/javascript, */*; q=0.01",
           "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
           "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
           "sec-fetch-dest": "empty",
           "sec-fetch-mode": "cors",
           "sec-fetch-site": "same-origin",
           "x-requested-with": "XMLHttpRequest",
           "cookie": cookie}

id_url = 'https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsCxsq/getCxsq'
apply_url = 'https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsCxsq/saveCxsq'

id_form_data = "info=%7B%22id%22%3A%22id%22%7D"

c = Calendar(firstweekday=1)

for date in c.itermonthdates(2021,9):
    datepart = str(date).split('-')
    if int(datepart[1]) == 9 and int(datepart[-1]) > 14:
        id_response = requests.post(id_url, id_form_data, headers=headers)
        apply_id = id_response.json()['module']['id']
        apply_form_data = 'info=%7B%22model%22%3A%7B%22rq%22%3A%22{}%22%2C%22cxly%22%3A%22%E4%BD%93%E6%A3%80%22%2C%22cxlx%22%3A%2201%22%2C%22yjlxjsrq%22%3A%22%22%2C%22id%22%3A%22{}%22%2C%22lsjcjg%22%3A%22%22%2C%22lsbgcjyy%22%3A%22%22%2C%22lsjcsj%22%3A%22-undefined-undefined%22%2C%22lsljjkmys%22%3A%22%22%2C%22lsdsjxcmys%22%3A%22%22%7D%7D'.format(str(date), apply_id)
        apply_response = requests.post(apply_url, apply_form_data, headers=headers)
        print(apply_response)

