from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html')

def qa_view(request):
    return render(request, 'blog/qa.html')
