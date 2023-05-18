from django.shortcuts import render, redirect

from .models import Request, Reply
from .forms import RequestForm, ReplyForm

def index(request):
    """助っ人掲示板のホームページ"""
    requests = Request.objects.order_by('date_added')
    replies = Reply.objects.order_by('date_added')
    context = {'requests': requests, 'replies': replies}
    return render(request, 'helper_board_app/index.html', context)

def user_page(request, user_id):
    """受け取ったuser_idのUserのページを表示する"""
    user = Request.objects.get(pk=user_id).owner
    # ユーザーの持つ求人に紐づけられたリプライだけを取得
    replies = Reply.objects.filter(request=Request.objects.get(pk=user_id))
    # ユーザーの持つ求人のみを取得
    requests = Request.objects.filter(owner=user)
    context = {'requests': requests,
               'owner': user,
               'replies': replies,
               }
    return render(request, 'helper_board_app/user_page.html', context)

def new_request(request):
    """助っ人を募集するためのページ"""
    if request.method != 'POST':
        form = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            # リクエストモデルに必要な補足情報を付け加えてから保存する
            new_request = form.save(commit=False)
            new_request.owner = request.user
            new_request.save()

            return redirect('helper_board_app:index')
        
    context = {'form': form}
    return render(request, 'helper_board_app/new_request.html', context)

def replies(request):
    """リプライを処理する"""
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            # リプライのテキスト以外に必要な属性を追加してからリプライを保存する
            reply = form.save(commit=False)
            reply.owner = request.user
            reply.request = Request.objects.get(pk=request.POST["request"])
            reply.save()

        return redirect('helper_board_app:index')

    
