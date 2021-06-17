from dateutil.relativedelta import relativedelta
import datetime

dateformat = "%Y.%m.%d"
dateformatnso = "%Y%m%d"
today = datetime.datetime.now()
num = 1


tm = datetime.datetime(2021,1,1) - relativedelta(months=num)
tmp = tm.strftime(dateformat)
tmpnso = tm.strftime(dateformatnso)
beday= datetime.datetime(2021,1,1) - relativedelta(months=(num+1))
bmp = beday.strftime(dateformat)
bmpnso = beday.strftime(dateformatnso)

print(tmp)
print(bmp)