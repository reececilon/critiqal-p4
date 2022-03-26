from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review
from .forms import CommentForm

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
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
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

    def post(self, request, slug):
        review = get_object_or_404(Review, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_content', args=[slug]))


def NotFound(request, exception):
    return render(request, 'not-found.html')


def ErrorFive(request, exception):
    return render(request, 'error-500.html')
