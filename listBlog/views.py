from django.shortcuts import render

from listBlog.models import Category


def blogs(request):
    categories = Category.objects.all().prefetch_related('blog_set')
    return render(request, "blog_view.html",{'categories' : categories})