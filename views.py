from django.shortcuts import render

from .models import apt


# def post_list(request):
#     apt_list = apt.objects.order_by('apt_name')[0:5]
#     template = loader.get_template('aptmanager/post_list.html')
#     context = {'apt_list : apt_list'}
#     return HttpResponse(template.render(context, request))

def post_list(request):
    # candidates = apt.objects.all()
    text = 'new'
    return render(request, 'aptmanager/post_list.html', {'message': text})


def new_apt_list(request):
    apt_name = apt.objects.all()
    context = {'apt_name': apt_name}
    return render(request, 'aptmanager/new_apt_list.html', context)
