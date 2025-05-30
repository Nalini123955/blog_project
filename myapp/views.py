from django.shortcuts import render
def custom_page_not_found(request):
    return render(request, 'index.html', status=404)


