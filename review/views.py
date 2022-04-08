from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review
from .forms import CommentForm


class ReviewList(generic.ListView):
    """Creates a list of the available
    reviews that are not drafted and paginates them"""
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 8


class ReviewInfo(View):
    """Returns the review model information,
    comments, and likes. Also Checks if the
    user liked the post."""

    def get(self, request, slug, *args, **kwargs):
        """Checks whether the user liked review,
        and returns Review model information"""
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
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Post form for the user to comment on a review"""
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_date')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted for approval!')
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_content.html",
            {
                'review': review,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
                'liked': liked,
            },
        )


class ReviewLike(View):
    """Enables the user to like a review"""

    def post(self, request, slug):
        """Enables the user to like or unlike depending
        on whether the user has previously liked a review"""
        review = get_object_or_404(Review, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_content', args=[slug]))


def not_found(request, exception):
    """Returns the custom 404 error page (not-found.html)"""
    return render(request, 'not-found.html')


def error_five(request):
    """Returns the custom 500 error page (error-500.html)"""
    return render(request, 'error-500.html')
