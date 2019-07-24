import quandl
quandl.ApiConfig.api_key = '_ogqx1Zunwxz-8eij_x7'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': '2019-1-1', 'lte': '2019-12-31' }, 
                        paginate=True)
data.head()

# create a new dataframe with 'date' column as index
new = data.set_index('date')

# use pandas pivot function to sort adj_close by tickers
clean_data = new.pivot(columns='ticker')

# check the head of the output
# print(clean_data.head())

print(quandl.get("FRED/GDP", start_date="2019-01-01", end_date="2019-07-18"))

print(quandl.get("WIKI/MSFT", rows=5))
