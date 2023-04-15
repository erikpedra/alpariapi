# alpariapi
Alpari API

# Sosial Media
Telegram : https://t.me/minsanztuy
Website    : https://autotradevip.com/en/  
Olmyptrade : https://youtu.be/zTZT7zDlmtU  
Binomo     : https://youtu.be/ww9rVMX5TK4  
IQ Option  : https://youtu.be/4i3YUEDRGWY  
Quotex     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA  
Expert Option     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA
Alpari     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA  

### Import
```python
from alpariapi.stable_api import Alpari 
```
### Login by ssid
```python
from alpariapi.stable_api import Alpari  
ssid="""23124343254324729374983274"""
user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"#make sure is value is same as you login web, the alpari is check that.
account=Alpari(set_ssid=ssid,user_agent=user_agent)
account_id=1234556
check,message=account.connect(account_id)
```
```
