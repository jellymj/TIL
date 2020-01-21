Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import wwebbrowser
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import wwebbrowser
ModuleNotFoundError: No module named 'wwebbrowser'
>>> import webbrowser
>>> webbrowser.open(www.google.com)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    webbrowser.open(www.google.com)
NameError: name 'www' is not defined
>>> webbrowser.open(https://www.google.com)
SyntaxError: invalid syntax
>>> import webbrowser
>>> webbrowser.open(https://www.google.com)
SyntaxError: invalid syntax
>>> webbrowser.open(https//www.google.com)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    webbrowser.open(https//www.google.com)
NameError: name 'https' is not defined
>>> webbrowser.open("www.google.com")
True
>>> webbrowser.open("https://www.google.com")
True
>>> webbrowser.open("https://www.naver.com")
True
>>> webbrowser.open("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%8B%B8%ED%94%BC")
True
>>> site = {'딸기', '바나나', '스타벅스'}
for i in site:
     webbrowser.open("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + site)
     
SyntaxError: multiple statements found while compiling a single statement
>>> site = {'딸기', '바나나', '스타벅스'}
>>> for i in site:
	webbrowser.open("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + i)

	
True
True
True
>>> import requests
>>> requests
<module 'requests' from 'C:\\Users\\multicampus\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\requests\\__init__.py'>
>>> requests.get(https://finance.naver.com/sise/).status_code
SyntaxError: invalid syntax
>>> requests.get(finance.naver.com/sise/).status_code
SyntaxError: invalid syntax
>>> requests.get(www.finance.naver.com/sise/).status_code
SyntaxError: invalid syntax
>>> requests.get(www.finance.naver.com/sise).status_code
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    requests.get(www.finance.naver.com/sise).status_code
NameError: name 'www' is not defined
>>> requests.get("https://finance.naver.com/sise").status_code
200
>>> requests.get("https://finance.naver.com/sise").text

>>> response = requests.get("https://finance.naver.com/sise").text
>>> print(response)

>>> 
