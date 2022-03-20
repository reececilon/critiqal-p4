from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 8


class ReviewInfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_date')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'review_content.html',
            {
                'review': review,
                'comments': comments,
                'liked': liked,
            },
        )

