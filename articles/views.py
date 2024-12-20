from django.shortcuts import render, redirect
from articles.models import Article# Use absolute import
from .forms import ContactForm, CommentForm
from .models import Video
from .models import CommunityPost, CommunityCategory
from .forms import CommunityPostForm

def home_view(request):
    return render(request, 'home.html')

def article_list(request):
    articles = Article.objects.all().order_by('-date_published')
    return render(request, 'articles/article_list.html', {'articles': articles})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')  # Success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'articles/article_detail.html', {
        'article': article, 
        'comments': comments,
        'form': form
    })

def video_list(request):
    videos = Video.objects.all().order_by('-date_published')  # Fetch videos ordered by date
    return render(request, 'videos/video_list.html', {'videos': videos})



# View to display all community posts
def community_view(request):
    categories = CommunityCategory.objects.all()
    selected_category = request.GET.get('category', None)

    if selected_category:
        posts = CommunityPost.objects.filter(category__name=selected_category)
    else:
        posts = CommunityPost.objects.all()

    return render(request, 'community_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': selected_category
    })

# View to add a new post
def add_post(request):
    if request.method == 'POST':
        form = CommunityPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community')  # Redirect back to the community list
    else:
        form = CommunityPostForm()
    return render(request, 'add_post.html', {'form': form})


def about_view(request):
    return render(request, 'about.html')

