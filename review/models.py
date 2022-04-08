from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))
RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    rating = models.IntegerField(choices=RATING, default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)
    excerpt = models.CharField(max_length=80, blank=True)
    yt_link = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def no_of_likes(self):
        return self.likes.count()

    def get_iframe(self):
        if self.yt_link and 'youtube' in self.yt_link and '=' in self.yt_link:
            part_1 = self.yt_link.split('=', 1)[1]
            if '&' in part_1:
                return part_1.split('&', 1)[0]
            else:
                return part_1
        else:
            return None


class Comment(models.Model):
    post = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.body} - {self.name}'
