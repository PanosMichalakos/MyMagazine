from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from next_prev import next_in_order, prev_in_order
from .forms import CommentForm, PostForm
from .models import Post, Category, Author, PostView
from marketing.models import Signup


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists:
        return qs[0]
    return None


def search(request):
    categories = Category.objects.all()
    posts = posts = Post.objects.order_by('-timestamp')
    query = request.GET.get('query')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'search.html', context)


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-timestamp')

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'categories': categories,
        'posts': posts
        # 'form': form
    }
    return render(request, 'index.html', context)


def news(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-timestamp')
    paginator = Paginator(posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'categories': categories,
        'page_request_var': page_request_var,
        'posts': paginated_queryset
    }
    return render(request, 'news.html', context)


def category(request, category):
    posts = Post.objects.order_by('-timestamp').filter(categories=category)
    context = {
        'posts': posts
    }
    return render(request, 'category.html', context)


def gallery(request):
    context = {
    }
    return render(request, 'gallery.html', context)


def article(request, id):
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    posts = Post.objects.order_by('-timestamp')
    current_post = Post.objects.get(pk=id)
    next_post = next_in_order(current_post)
    previous_post = prev_in_order(current_post)
    form = CommentForm(request.POST or None)
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("article", kwargs={
                'id': post.pk
            }))
    context = {
        'post': post,
        'current_post': current_post,
        'next_post': next_post,
        'previous_post': previous_post,
        'categories': categories,
        'posts': posts,
        'form': form
    }
    return render(request, 'article.html', context)


def article_create(request):
    title = 'Create'
    categories = Category.objects.all()
    posts = Post.objects.order_by('-timestamp')
    author = get_author(request.user)
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("article", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'posts': posts,
        'categories': categories,
        'form': form
    }
    return render(request, 'article_create.html', context)


def article_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    posts = Post.objects.order_by('-timestamp')
    author = get_author(request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("article", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'posts': posts,
        'post': post,
        'categories': categories,
        'form': form
    }
    return render(request, 'article_create.html', context)


def article_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("news"))
