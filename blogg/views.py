from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer

from .models import Post, Voting


def get_list(request):
    return JsonResponse([{'name': "Aticle", 'description': 'asdkhnaksjdnkjasdnkjansd jansd kjansdk js'}], safe=False)


def get_post(request):
    # obj = Post.objects.first()
    # return JsonResponse({
    #     "name": obj.name_post,
    #     "text": obj.text,
    #     "author": obj.author_post.username,
    #     'time created': obj.time_created
    # })
    response = []
    for obj in Post.objects.all():
        response.append({
            "id": obj.id,
            "name": obj.name_post,
            "text": obj.text,
            "author": obj.author_post.username,
            'time created': obj.time_created
        })

    return JsonResponse({'response': response})


def get_voting(request, post_id):
    obj = Voting.objects.get(id=post_id)
    return JsonResponse({
        "vote": obj.vote
    })
