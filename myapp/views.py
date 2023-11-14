from django.shortcuts import render
from myapp.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse

def form_view (reequest):
    form = CommentForm()

    if (reequest.method) == 'POST':
        form = CommentForm (request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComments (
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    
    return render(reequest, 'blog.html', {'form': form})
# Create your views here.
