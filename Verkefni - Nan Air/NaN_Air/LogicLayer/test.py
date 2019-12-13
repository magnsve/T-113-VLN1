import dateutil.parser
import datetime
date = '2019-12-12 08:00:01'
test = dateutil.parser.parse(date) + datetime.timedelta(hours=4)
print(test)