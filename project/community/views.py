from django.shortcuts import render
from .models import Post
from .models import Financial
from .models import Notice
from .models import Donations_Report
from .models import History
# Create your views here.

# 메인화면 
def home(request):
	return render(request, 'home.html')

# 스케쥴
def schedule(request):
    return render(request, 'schedule.html')

    
def donation(request):
    return render(request, 'donation.html')

def contact(request):
    return render(request, 'contact.html')

def board(request):
    return render(request, 'board.html')

def gallery(request):
    return render(request, 'gallery.html')

def ci(request):
    return render(request, 'ci.html')

def greeting(request):
    return render(request, 'greeting.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'blog.html', {'postlist':postlist})

def notice(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Notice.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'notice.html', {'postlist':postlist})

def financial(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Financial.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'financial.html', {'postlist':postlist})

def history(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = History.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'history.html', {'postlist':postlist})

def donat_report(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Donations_Report.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'donat_report.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})

def notice_posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Notice.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})

def financial_posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Financial.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})

def donat_posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Donations_Report.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})

def history_posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = History.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'posting.html', {'post':post})