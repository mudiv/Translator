# Programming By : RUKS
# Instagram: _v_go
# Telegram : @DIBIBl
# Telegram2 : @TDTDI
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# automatic reaction tool
import requests
import urllib
k=input(" Enter text in English :")
def translate(fr, to, text):
	url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={fr}&tl={to}&hl=en-US&dt=t&dt=bd&dj=1&source=icon&tk=310461.310461&q=" + urllib.parse.quote_plus(str(text))
	response = requests.get(url).json()
	ruk=response['sentences'][0]["trans"]
	return ruk
print("~"*10)
print(translate("en", "ar", k) )

# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	