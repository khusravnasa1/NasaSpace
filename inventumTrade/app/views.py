from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm, ReviewForm
from .models import Profile, ReviewRating
from django.contrib import messages


def page(request):
    all_files = Profile.objects.all()

    context = {
        'all_files' : all_files,
    }

    if request.POST:
        print(request.POST.get('title'))

        print(request.POST.get('file'))
        Profile.objects.create(title=request.POST.get('title'), file=request.FILES.get('file')),


    return render(request, 'add_post.html', context)

def home(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'single_project.html')

def view_project(request):
    return render(request, "view_page.html")

"""
def submit_review(request, research_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.filter(user__id=request.user.id, research__id=research_id).first()
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = research_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                #return redirect(url)


"""