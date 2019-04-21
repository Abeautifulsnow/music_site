from django.db import models
import datetime

# Create your models here.


class Label(models.Model):
    """"歌曲分类表"""
    label_id = models.AutoField('序号', primary_key=True)
    label_name = models.CharField('分类标签', max_length=10)

    class Meta:
        verbose_name = '歌曲分类'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.label_name


class Song(models.Model):
    """"歌曲信息表"""
    song_id = models.AutoField('序号', primary_key=True)
    song_name = models.CharField('歌曲名字', max_length=50)
    song_singer = models.CharField('歌手', max_length=50)
    song_album = models.CharField('专辑', max_length=50)
    song_time = models.CharField('时长', max_length=10)
    song_languages = models.CharField('语种', max_length=20)
    song_type = models.CharField('类型', max_length=20)
    song_release = models.CharField('发行时间', max_length=20)
    song_img = models.CharField('歌曲图片', max_length=20)
    song_lyrics = models.CharField('歌词', max_length=50, default='暂无歌词')
    song_file = models.CharField('歌曲文件', max_length=50)
    song_label = models.ForeignKey(Label, on_delete=models.CASCADE, verbose_name='歌曲分类')

    class Meta:
        verbose_name = '歌曲信息'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.song_name


class Dynamic(models.Model):
    """歌曲动态表"""
    dynamic_id = models.AutoField('序号', primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    dynamic_plays = models.IntegerField('播放次数', default=0)
    dynamic_search = models.IntegerField('搜索次数', default=0)
    dynamic_down = models.IntegerField('下载次数', default=0)

    class Meta:
        verbose_name = '歌曲动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.song.song_name


class Comment(models.Model):
    comment_id = models.AutoField('序号', primary_key=True)
    comment_text = models.CharField('内容', max_length=500)
    comment_user = models.CharField('用户', max_length=20)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='歌名')
    comment_date = models.DateTimeField('日期', auto_now_add=True)

    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.song.song_name


class Banner(models.Model):
    """"轮播图"""
    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', max_length=100, upload_to="banner/%Y/%m")
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.datetime.now)

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.title