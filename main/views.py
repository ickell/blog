from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone

from .models import Post, Comment
from .form import PostForm

def home(request):
    posts = Post.objects.order_by('-date')

    context = {
        'posts' : posts,
    }

    return render(request, 'home.html', context)

def search(request):
    word = request.GET.get('q')

    searched = Post.objects.filter(Q(title__icontains = word))
    return render(request, 'search.html', {'searched':searched})

def write(request):
    return render(request, 'write.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.save()

    return redirect('/')

def detail(request, post_id):
    post = get_object_or_404(Post, pk =post_id)

    var = {
        'posts':post,
    }
    return render(request, 'detail.html', var)

def delete(request, post_id):
    posts = get_object_or_404(Post, pk =post_id)
    posts.delete()
    return redirect('/')


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
    
        if form.is_valid():
            post = form.save(commit=False)
            # 저장하기전 상태의 데이터값을 자동으로 form에 채워줌
            post.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'update.html', {'form': form})

def comment_write(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST.get('content')
        Comment.objects.create(post=post, comment_contents=content)
        return redirect('/n/' + str(post.id))