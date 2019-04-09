from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post, Event, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth import get_user_model
from .forms import CommentReplyForm, AddPostForm

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
User = get_user_model()
# Create your views here.

class PostListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'grievance.view_post'
    model = Post
    context_object_name = 'posts'
    template_name = 'grievance/complaints/posts.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-upvote')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['user'] = User.objects.filter(email=self.request.user.email)
        return context

# class AddCommentView(LoginRequiredMixin,CreateView):
#     model = Comment
#     form_class = CommentReplyForm
#     template_name = 'grievance/complaints/comment_reply_form.html'

class PostCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'grievance.add_post'
    form_class = AddPostForm
    template_name = 'grievance/complaints/post_form.html'
    model = Post

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        initial['author'] = self.request.user

        return initial

# class EventListView(ListView):
#     model = Event
#     context_object_name = 'events'
#     template_name = 'blog/events/events.html'

@login_required
@permission_required('grievance.add_comment')
def admin_reply_comment(request, pk):
    parent = get_object_or_404(Comment, pk=pk)
    post = parent.post
    if request.method == "POST":
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.parent_comment = parent
            comment.save()
            return redirect('grievance:post_list')
    else:
        form = CommentReplyForm()
    return render(request, 'grievance/complaints/comment_reply_form.html', {'form': form})

@permission_required('grievance.add_comment')
def add_comment_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('grievance:post_list')
    else:
        form = CommentReplyForm()
    return render(request, 'grievance/complaints/comment_reply_form.html', {'form': form})




@login_required
@permission_required('grievance.view_post')
def add_upvotes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.upvote += 1
    post.save()

    return HttpResponseRedirect(reverse('grievance:post_list'))


    # def get_queryset(self):
    #     # super().get_queryset()
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
