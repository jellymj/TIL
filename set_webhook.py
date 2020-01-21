import requests

token = '1059371526:AAFU5jfv1u5RUYltAtP7kaFRk9YeJn-fZNo'
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = 'https://d67e70dd.ngrok.io'
pythonanywhere_url = 'https://jellydong14.pythonanywhere.com/'
# set_webhook_url = f'{app_url}/setWebhook?url={ngrok_url}/telegram'
set_webhook_url = f'{app_url}/setWebhook?url={pythonanywhere_url}/telegram'

response = requests.get(set_webhook_url)
print(response)