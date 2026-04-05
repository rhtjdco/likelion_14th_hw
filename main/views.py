from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {                           
            'weather': '맑음',
            'feeling': '빨리 뒷풀이가 가고 싶음.',
            'note': '좀만 더 화이팅!'
        },
        'TLS': [
            "<strong>URL 연결:</strong> {% url '이름' %} → 주소를 직접 쓰지 않고 설정한 이름으로 연결",
            "<strong>변수 사용:</strong> {{ 변수명 }} → 변수에 지정된 데이터를 화면에 출력",
            "<strong>반복문:</strong> {% for 변수명 in 배열 %} → 리스트 데이터를 순서대로 출력",
            "<strong>조건문:</strong> {% if 조건 %} → 조건에 따라 출력",
            "<strong>필터:</strong> {{ 변수|filter }} → 데이터를 필터에 대해 변환"
        ]
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')