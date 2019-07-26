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

`>>> from worldtradingdata import WorldTradingData`  
`>>> my_api_token = get_my_token_from_somewhere_safe()`  
`# provide the api_token once when creating the WorldTradingData instance.`  
`# you do not need to provide the api_token on each request`  
  
`>>> wtd = WorldTradingData(my_api_token)`  
`>>> wtd.stock_search('AAPL')  # will find all your favourite fruity stocks`

#### General Guidance
Required arguments should be given individually, and optional arguments should be 
supplied as a dictionary, with the param name as the key, and the param value as the value.

e.g.
Perform a basic stock search with  
`wtd.stock_search('AAPL')`

Anything which is an optional query string param in the official docs can be passed in a dictionary 
as a second argument 
([see official docs for full argument reference](https://www.worldtradingdata.com/documentation#stocks-and-indexes)).

`optional_params = {'output': 'csv', 'currency': 'usd'}`  
`wtd.stock_search('AAPL', optional_params)`


Methods have been named in accordance with the url path suffix for that request in the official docs. 
i.e. if the base url of a request is
`https://api.worldtradingdata.com/api/v1`
 and the final url for a Forex History request is 
`https://api.worldtradingdata.com/api/v1/forex_history`
then the url path suffix of the request is considered to be `/forex_history`.  

All the methods in the SDK are named according to their corresponding url path suffix without the `/`.  
e.g. `wtd.forex_history(args, in, here)` 



## Method Reference

Please be aware that this SDK is designed to be a loose wrapper around the official REST API 
provided by www.worldtradingdata.com .
That means that it does not include pre-flight checks to make sure your provided arguments are correct. 
This provides much more flexibility, but it means if you provide poorly formed arguments 
to the SDK, they will be ignored and the results you get might not be what you expect.

I'm working on stricter type checking for version 2.

\# note: 'api_token' is supplied automatically

### Real Time Market Data
_full reference at [https://www.worldtradingdata.com/documentation#real-time-market-data](https://www.worldtradingdata.com/documentation#real-time-market-data)_   
**Stock and Index Real Time**  
`wtd.stock(symbol: list [, optional_params: dict])`  
_example_  
`more_params = {'output': 'csv'}`  
`wtd.stock(['AAPL', 'GOOG'], more_params)`

**Mutual Fund Real Time**  
`wtd.mutual_fund(symbol: list [, optional_params: dict])`  
_example_  
`my_symbol_array = ['AAAAX', 'AAADX', 'AAAGX']`  
`wtd.mutual_fund(my_symbol_array)`  

### Intraday Market Data
_full reference at [https://www.worldtradingdata.com/documentation#intraday-market-data](https://www.worldtradingdata.com/documentation#intraday-market-data)_
**Stock and Index Intraday**  
`wtd.intraday(symbol: str, interval: int, range: int [, optional_params: dict])`  

### Historical Market Data
**Full History**  
`wtd.history(symbol: str [, optional_params: dict])`  

**Multi Single Day History**  
`wtd.history_multi_single_day(symbol: str, date: str [, optional_params: dict])`  
`# date should be formatted as 'YYYY-MM-DD'`  

### Forex
**Real Time**  
`wtd.forex(base: str)`  

**Historical**  
`wtd.forex_history(base: str, convert_to: str [, optional_params: dict])`  

**Single Day History**  
`wtd.forex_single_day(base: str, date: str [, optional_params: dict])`  

### Searching Stocks  
`wtd._stock_search(search_term: string [, optional_params: dict])`  

Perform a basic stock search with  
`wtd.stock_search('AAPL')`  

Anything which is a query_string param in the official docs can be passed 
in the dictionary of optional params ([see official docs for searching](https://www.worldtradingdata.com/documentation#stocks-and-indexes))

`optional_params = {'output': 'csv', 'currency': 'usd'}`  
`wtd.stock_search('AAPL', optional_params)`  

