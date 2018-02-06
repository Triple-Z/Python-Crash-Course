from .models import Topic


def check_topic_owener(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.user == topic.owner:
        return True
    else:
        return False
