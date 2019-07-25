# World Trading Data Python SDK

**This is an _UNOFFICIAL_ SDK. That means that neither this repo nor the author have any 
relationship with World Trading Data. This repo is simply a tool built to make it easier to 
integrate with the rest API.**

_This SDK is designed to access financial data. Therefore the author would like to stress that 
what you do with any data you may get through this SDK is your problem and yours alone. I take 
absolutely zero responsibility for any losses or problems that may arise from using this SDK_

### Getting Started

This SDK will require you to have an account with World Trading Data (sign up 
[here](https://www.worldtradingdata.com))

Be advised, there are as yet no stable releases for this package and it is 
100% definitely still in development and breaking changes (while avoided) may be deployed 
at any time. You have been warned.

#### Installation
1.  Make sure you have pip installed
2.  In the console `pip install worldtradingdata`


then in python...

\>>> from worldtradingdata import WorldTradingData

\>>> my_api_token = get_my_token_from_somewhere_safe()

\# provide the api_token once when creating the WorldTradingData instance. \
\# you do not need to provide the api_token on each request 

\>>> wtd = WorldTradingData(my_api_token)

\>>> wtd.search_stock('AAPL')
\# will find all your favourite fruity stocks


### Method Reference

Please be aware that this SDK is designed to be a loose wrapper around the official REST API 
provided by www.worldtradingdata.com .
That means that it does not include pre-flight checks to make sure you provided arguments are correct. 
This method provides much more flexibility, but it means if you provide poorly formed arguments 
to the SDK, it will send them and you'll get an error in the 
returned data, not locally.

#### Forex
###### Real Time
`wtd.forex(base: str)`

Args\
base: currency code for which exchange rate data will be returned, e.g., "USD"

###### Historical
`wtd.forex_history(base: str, convert_to: str)`

Args\
base: Base of the currency you wish to return data for.
convert_to: Value of the currency you wish to return conversion data to.

###### Single Day History
wtd.forex_single_day
#### Searching Stocks
wtd.search_stocks(search_term: string [, optional_params: dict])

Perform a basic stock search with\
`wtd.search_stock('AAPL')`

Anything which is a query_string param in the official docs can be passed as a 
second argument ([see official docs for searching](https://www.worldtradingdata.com/documentation#stocks-and-indexes))

\# note: 'search_term' and 'api_token' are supplied automatically\
`optional_params = {'output': 'csv', 'currency': 'usd'}`
`wtd.search_stocks('AAPL', optional_params)`


