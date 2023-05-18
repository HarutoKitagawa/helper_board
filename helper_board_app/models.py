from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """募集中のカテゴリーを表す"""
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = 'categories'

class Request(models.Model):
    """助っ人求人を表す"""
    text = models.CharField(max_length=200)
    detail = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)
    # 誰の求人かの情報
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # 求人のカテゴリー
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        """モデルの文字列表現を表す"""
        return self.text
    
class Reply(models.Model):
    """求人への返信を表す"""
    text = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)
    # 誰のリプライかの情報
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # どの求人へのリプライかの情報
    request = models.ForeignKey(Request, on_delete=models.CASCADE)