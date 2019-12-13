import dateutil.parser
import datetime
date = '2019-11-02T23:21:00'
test = dateutil.parser.parse(date) + datetime.timedelta(hours=4)
print(test)