from django.db import models

class HomePageInfo(models.Model):
    abstract_text = models.TextField()

    def __str__(self):
        return "Home Page Information"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()  # Link to the video (e.g., YouTube or Vimeo)
    description = models.TextField(blank=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CommunityCategory(models.Model):
    name = models.CharField(max_length=50)  # e.g., 'AI', 'Technology', 'Business'

    def __str__(self):
        return self.name

# Model for Community Posts
class CommunityPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(CommunityCategory, on_delete=models.CASCADE, related_name='posts')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='Anonymous')  # Optional: Add user functionality later

    def __str__(self):
        return self.title
