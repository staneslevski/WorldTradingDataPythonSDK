# World Trading Data Python SDK

**This is an _UNOFFICIAL_ SDK. That means that neither this repo nor the author have any 
relationship with World Trading Data. This repo is simply a tool built to make it easier to 
integrate with the rest API.**

_This SDK is designed to access financial data. Therefore the author would like to stress that 
what you do with any data you may get through this SDK is your problem and yours alone. I take 
absolutely zero responsibility for any losses or problems that may arise from using this SDK_

##### Full docs are at https://staneslevski.github.io/WorldTradingDataPythonSDK/



### Getting Started

This SDK will require you to have an account with World Trading Data (sign up 
[here](https://www.worldtradingdata.com))

#### Installation
1.  Make sure you have pip installed
2.  In the console `pip install worldtradingdata`

then in python...

\>>> from worldtradingdata import WorldTradingData

\>>> my_api_token = get_my_token_from_somewhere_safe()

\>>> wtd = WorldTradingData(my_api_token)

\>>> wtd.search_stock('AAPL')
\# will find all your favourite fruity stocks


For full reference, please see the docs at https://staneslevski.github.io/WorldTradingDataPythonSDK/

enjoy!


