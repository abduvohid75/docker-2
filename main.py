import requests
import time
times = 10
while times > 0:
    response = requests.get("https://google.com")
    time.sleep(5)
    print(response.text)
else:
    print("End")
    
