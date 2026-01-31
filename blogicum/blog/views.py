import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post

POST_COUTN = 5


def set_published_post(querry_set):
    return (
        querry_set.
        filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.datetime.now()
        ))


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.all()
    context = {
        'post_list': set_published_post(post_list,)[:POST_COUTN]
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post_list = Post.objects.all()
    context = {
        'post': get_object_or_404(set_published_post(post_list,), pk=id)
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category.objects.all(), slug=category_slug,
                                 is_published=True)
    return render(request, template_name, {
        'category': category,
        'post_list': set_published_post(category.posts,)},)
