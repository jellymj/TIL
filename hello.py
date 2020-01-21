from flask import Flask, render_template, request
from datetime import datetime
import random
import requests
from flask import Flask
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY'

from datetime import datetime

#11월 29일까지 d-day 출력
@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2020, 11, 29)
    td = endgame - today
    return f'{td.days}일 남았습니다'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1> 여러 줄을 보내봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    <ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다, {name}님!'
    return render_template('greeting.html', html_name=name) #각각 렌더링할 파일 이름, 이름변수

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    # return f'{number} 의 세제곱은 {result} 입니다.'
    return render_template('cube.html', result = result, number = number)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['시래기된장국', '김볶밥', '라면', '자장면']
    order = random.sample(menu, people)
    return str(order)    

@app.route('/movie')
def movies():
    movies = ['포드v페라리', '우리형', '겨울왕국', '탕수육']
    return render_template('movie.html', movies = movies) 

@app.route('/ping')
def ping():
    return render_template('ping.html')     

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html = age)

#네이버, 구글에서 검색한 창 뜨게
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

#@app.route('/gotmademe')
#def gotmademe():
#    gotmademe = ['걍웃김', '게으름', '똑똑해', '매력']
#    answer = random.sample(gotmademe, 2)
#    return render_template('gotmademe.html', answer = answer)


@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list = ['잘생김', '못생김', '평범함']
    second_list = ['자신감', '쑥스러움', '애교', '잘난척']
    third_list = ['허세', '돈복', '식욕', '물욕']

    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)

    return render_template('godmademe.html', html_in_name=name, first = first, second = second, third = third)

@app.route('/bday')
def bday():
    today = datetime.now()
    bday = datetime(2020, 1, 14)
    
    if bday == today:
        return f'네.'
    else:
        return f'아니요.'

@app.route('/isitbirth')
def isitbirth():
    today = datetime.now()
    if today.month == 1 and today.day == 16:
        result = True
    else:
        result = False
    return render_template('isitbirth.html', result = result)    

@app.route('/throw')
def throw():
    return render_template('throw.html')

@app.route('/ascii')
def ascii():
    url = 'http://artii.herokuapp.com/'
    word = request.args.get('word')
    result = requests.get(f'{url}make?text={word}').text
    return render_template('ascii.html', result = result)

@app.route('/dust')
def dust():
    api_key = 'mbsr22ZxsnSdYzgWL6ZEXF8zchZReHHj06FVrZEaYhzLx14roDMN0DLdr%2FCNzC4K5i1s3UmmeNZ3VEvoGtg0%2BQ%3D%3D'
    url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&numOfRows=40&pageNo=1&startPage=3&sidoName=서울&ver=1.6'
    
    today = datetime.now()
    response = requests.get(url).text
    data = BeautifulSoup(response, 'xml')
    location = data('item')[27] #강남구

    dust = int(location.pm10Value.text)
    station = location.stationName.text

    if 150 < dust:
        dust_rate = '매우 나쁨'
    elif 80 < dust <= 150:
        dust_rate = '나쁨'
    elif 30 < dust <= 80:
        dust_rate = '보통'
    else:
        dust_rate = '좋음'
    return render_template('dust.html', station = station, dust_rate = dust_rate, today = today)

#맨 밑에 있어야함!!!   
if __name__ == '__main__':
    app.run(debug = True)
