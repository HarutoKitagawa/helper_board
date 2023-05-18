"""helper_board_appのURLパターン定義"""

from django.urls import path

from . import views

app_name = 'helper_board_app'

urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # ユーザーページ
    path('mypage/<int:user_id>', views.user_page, name="user_page"),
    # 助っ人募集ページ
    path('new_request/', views.new_request, name="new_request"),
    # リプライの処理
    path('replies/', views.replies, name="replies"),
]