import datetime
from dateutil.parser import parse

num = 0
while True:
    num += 1
    #获取当前时间
    now_date = parse(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #now_date = datetime.datetime.strptime('2020-9-23 18:00:00', '%Y-%m-%d %H:%M:%S')
    #获取页面开始时间
    web_date = datetime.datetime.strptime('2020-10-07 12:21:00', '%Y-%m-%d %H:%M:%S')
    #获取倒计时时间
    a = int(65)
    #获取最后时间
    if num >= 2:
        web_date2 = parse((web_date + datetime.timedelta(hours=(a-2)*(num-1))).strftime("%Y-%m-%d %H:%M:%S"))
        last_date = parse((web_date2 + datetime.timedelta(hours=a)).strftime("%Y-%m-%d %H:%M:%S"))
    else:
        last_date = parse((web_date + datetime.timedelta(hours=a)).strftime("%Y-%m-%d %H:%M:%S"))

    #计算倒计时秒数
    dtime = (last_date - now_date).total_seconds()

    #将秒数换算成时分秒
    dostime = datetime.timedelta(seconds=dtime)

    if dtime > 7200:
        print(dostime)
        break










