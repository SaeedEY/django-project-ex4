from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post,Setting

def posts(request):
    conf = {
        'title' :    Setting.objects.get(option='blog_title').value,
        'about' :   Setting.objects.get(option='blog_about').value,
        'social_media'  :   Setting.objects.get(option='blog_social_media').value
        }
    the_posts = Post.objects.exclude(published_date = None).order_by('-published_date') # Dont Show the posts which they have not published yet
    return render(request,'blog/posts.html',{'posts':the_posts,'tags':Post.tags,'blog':conf})

def post(request,post_id):
    conf = {
        'title' :    Setting.objects.get(option='blog_title').value,
        'about' :   Setting.objects.get(option='blog_about').value,
        'social_media'  :   Setting.objects.get(option='blog_social_media').value
        }
    try:
        the_post = Post.objects.get(id=post_id)
    except:
        return HttpResponseRedirect('/404') # redirect to 404 page on `get(title=post_id)` exception
    return render(request,'blog/post.html',{'post':the_post,'tags':Post.tags,'blog':conf})

def tag(request,tag_name):
    conf = {
        'title' :    Setting.objects.get(option='blog_title').value,
        'about' :   Setting.objects.get(option='blog_about').value,
        'social_media'  :   Setting.objects.get(option='blog_social_media').value
        }
    try:
        the_posts = Post.objects.filter(tag=tag_name)
    except:
        return HttpResponseRedirect('/404') # redirect to 404 page on `get(title=post_id)` exception
    return render(request,'blog/tag.html',{'posts':the_posts,'tags':Post.tags,'blog':conf,'current_tag':tag_name})

def pnf404(request):
    return render(request,'blog/404.html',{})