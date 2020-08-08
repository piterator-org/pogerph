from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
	class Meta:
		#verbose_name_plural="Categories"
		verbose_name='分类'
		verbose_name_plural='分类'

	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Tag(models.Model):
	class Meta:
		verbose_name='标签'
		verbose_name_plural='标签'

	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Menu(models.Model):
	class Meta:
		verbose_name='菜单'
		verbose_name_plural='菜单'

	name=models.CharField(max_length=100)
	link=models.CharField(max_length=100,default='')
	order=models.PositiveSmallIntegerField()
	
	def __str__(self):
		return self.name

class Button(models.Model):
	class Meta:
		verbose_name='按钮'
		verbose_name_plural='按钮'

	name=models.CharField(max_length=100)
	url=models.URLField()
	order=models.PositiveSmallIntegerField()
	
	def __str__(self):
		return self.name

class Article(models.Model):
	class Meta:
		verbose_name='文章'
		verbose_name_plural='文章'
	
	title=models.CharField(verbose_name='标题',max_length=80,default='无标题')
	subtitle=models.CharField(verbose_name='副标题',max_length=80,default='')
	publish_date=models.DateTimeField(verbose_name='发布日期',default=timezone.now)#verbose_name='date published'
	url_mark=models.CharField(verbose_name='URL 标识',max_length=60)
	original_article_link=models.CharField(verbose_name='原文链接',max_length=100,default='')
	content=models.TextField(verbose_name='内容',default='')
	author=models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE,default=0)
	category=models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE,default=0)
	tag=models.ManyToManyField(Tag,verbose_name='标签',blank=True,default=0)
	
	def __str__(self):
		return self.title
