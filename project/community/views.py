from django.shortcuts import render
from .models import Post
# Create your views here.

# 메인화면 
def home(request):
	return render(request, 'home.html')

# 스케쥴
def schedule(request):
    return render(request, 'schedule.html')

    
def donation(request):
    return render(request, 'donation.html')

def beta(request):
    return render(request, 'beta.html')

def gamma(request):
    return render(request, 'gamma.html')

def contact(request):
    return render(request, 'contact.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})