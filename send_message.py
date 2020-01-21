import requests

# 기본 설정
token = '1059371526:AAFU5jfv1u5RUYltAtP7kaFRk9YeJn-fZNo'
app_url = f'https://api.telegram.org/bot{token}'

# 응답 내용 저장하기
update_url = f'{app_url}/getUpdates'
response = requests.get(update_url).json()
#print(response)

#chat_id 찾아서 꺼내기
chat_id = response.get('result')[0].get('message').get('chat').get('id')
text = '불금 화이팅'

message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
print(requests.get(message_url))