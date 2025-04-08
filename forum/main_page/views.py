from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject
from django.views.generic import ListView
from .forms import CommentForm, SearchForm, SubjectForm
from django.contrib.auth.models import User
from .models import Comment, Like
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

class SubjectsListView(ListView):
    context_object_name = 'subjects'
    model = Subject
    paginate_by = 3
    template_name = 'main_page/subject/list.html'

    def get_queryset(self):
        return Subject.published.all()

class CommentsListView(ListView):
    context_object_name = 'comments'
    model = Comment
    paginate_by = 2
    template_name = 'main_page/subject/detail.html'

def subject_detail(request, year, month, day, subject):
    subject = get_object_or_404(Subject, slug=subject,
                                   status=Subject.Status.PUBLISHED,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    comments = subject.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        if 'like' in request.POST and request.user not in subject.liked.all():
            like = Like.objects.create(user=request.user, subject=subject, value='Like')
            like.save()
        elif 'like' in request.POST and request.user in subject.liked.all():
            like = Like.objects.filter(user=request.user, subject=subject)
            like.delete() 

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.subject = subject
            new_comment.name = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'main_page/subject/detail.html', {'subject': subject, 'new_comment': new_comment, 'comments': comments, 'comment_form': comment_form})


def subject_create(request):
    new_subject = None
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)
        if subject_form.is_valid():
            new_subject = subject_form.save(commit=False)
            new_subject.author = request.user
            new_subject.slug = slugify(new_subject.title)
            new_subject.save()
            return redirect('/subject/')
    else:
        subject_form = SubjectForm()
    return render(request, 'main_page/subject/create_sub.html', {'new_subject': new_subject, 'subject_form': subject_form})


def subject_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Subject.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')
    return render(request, 
                  'main_page/subject/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})

def my_view(request, user_id):
    user = User.objects.get(id=user_id)
    subjects_user = Subject.objects.filter(author=user)
    return render(request, 'main_page/subject/profile.html', {'user': user, 'subjects_user': subjects_user})


def delete_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return render(request, 'main_page/subject/delete_subject.html')