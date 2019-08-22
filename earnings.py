import bql

bq = bql.Servive()

time_range = bq.func.range('2017-01-01','2019-08-08')

security = ['ALI PM Equity']

last = bq.data.px_last(dates=time_range)
high = bq.data.px_high(dates=time_range)
low =bq.data.px_low(dates=time_range)

request = bql.Request(security,[last,high,low])

response = bq.execute(request)

df = response[0].df()

df = df.dropna()

df['ALI PRICES'] = df['PX_LAST()dates=RANGE(2017-01-01,2019-08-08)']
del df['PX_LAST()dates=RANGE(2017-01-01,2019-08-08)']

df.head()

security_sm = ['SMPH PM Equity']

df_sm['SMPH PRICES'] = df_sm['PX_LAST()dates=RANGE(2017-01-01,2019-08-08)']
del df_sm['PX_LAST()dates=RANGE(2017-01-01,2019-08-08)']

df_sm.head()
