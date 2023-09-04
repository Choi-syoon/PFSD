import requests

nodemcu_ip = 'http://10.157.223.173'  # ip
angle = 90 # Servo POS

url = f'{nodemcu_ip}/pos={angle}d'

response = requests.get(url)

print(response.text)