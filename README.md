
For more information, check the docs folder.

# Toon and google home

In quby the offer a google home thing, just if you put together
the api.ai and the toon. 

For that, we have to create an agent in api.ai, and then connect it to our
toon api, using a middle man to catch the api.ai intent information,
and do something with the toon.

To save some money and time, I'm going to create an AWS lamda with Zappa, and
use that to translate between the api ai webhook and the toon.


# References

Toon documentation:
https://www.toonapi.com/documentation/toon-developer-journey
https://www.toonapi.com/documentation/api-walkthrough
https://www.toonapi.com/documentation/swagger-io



Zappa:  https://github.com/Miserlou/Zappa

Api AI webhook example: https://github.com/api-ai/fulfillment-webhook-translate-python/blob/master/app.py

API AI python client: https://github.com/api-ai/apiai-python-client

