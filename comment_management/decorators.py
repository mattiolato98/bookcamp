from django.http import HttpResponseForbidden

from comment_management.models import Topic, Comment


def topic_owner_only(func):
    """
    Decoratore per negare l'accesso a utenti non proprietari del topic.
    """
    def check_and_call(request, *args, **kwargs):
        topic = Topic.objects.get(pk=kwargs['pk'])
        if not topic.user_owner == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return check_and_call


def comment_owner_only(func):
    """
    Decoratore per negare l'accesso a utenti non proprietari del commento.
    """
    def check_and_call(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.user_owner == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return check_and_call
