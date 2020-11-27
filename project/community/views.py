from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.

# 메인화면 
def home(request):
    noticelist = Notice.objects.all()[:5]
    financiallist = Financial.objects.all()[:5]
    donatlist = Donations_Report.objects.all()[:5]
    projectlist = Project.objects.all()[:3]
    return render(request, 'home.html', {'noticelist':noticelist, 'financiallist':financiallist, 'donatlist':donatlist, 'projectlist':projectlist})

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

def rounding(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Round.objects.all()
    paginator = Paginator(postlist, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'rounding.html', {'postlist': postlist, 'posts':posts})


# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'blog.html', {'postlist':postlist})


def notice(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    noticelist = Notice.objects.all()
    paginator = Paginator(noticelist, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'notice.html', {'noticelist': noticelist, 'posts':posts})



def financial(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    financiallist = Financial.objects.all()
    paginator = Paginator(financiallist, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'financial.html', {'financiallist': financiallist, 'posts':posts})

def history(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    historylist = History.objects.all()
    paginator = Paginator(historylist, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'history.html', {'historylist': historylist, 'posts':posts})

def donat_report(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    donatlist = Donations_Report.objects.all()
    paginator = Paginator(donatlist, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'donat_report.html', {'donatlist': donatlist, 'posts':posts})


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


def project(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Project.objects.all()
    paginator = Paginator(postlist, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'project.html', {'postlist': postlist, 'posts':posts})

def project_posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Project.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'gallery_posting.html', {'post':post})

def news(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = News.objects.all()
    paginator = Paginator(postlist, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'news.html', {'postlist': postlist, 'posts':posts})

