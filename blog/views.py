from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Blog
from .forms import CommentForm


class BlogList(ListView):
    queryset = Blog.objects.order_by('-created_at')
    template_name = 'index.html'


def blog_detail(request, slug):
    template_name = 'blog_detail.html'
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog
            new_comment.save()
            return render(request, template_name, {'comments': comments,
                                                   'new_comment': new_comment,
                                                   'blog': blog})
        else:
            return render(request, template_name, {'blog': blog})
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'blog': blog,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class AuthorView(TemplateView):
    template_name = 'author.html'
