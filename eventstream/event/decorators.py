#:coding=utf-8:

from django.shortcuts import get_object_or_404

from models import Event

def event_view(f):
    """
    イベントオブジェクトを取得
    存在しない場合は、404 Not Found を返す
    """
    def _wrapped(request, event_id, *args, **kwargs):
        event = get_object_or_404(Event, pk=event_id)
        return f(request, event, *args, **kwargs)
    return _wrapped
    
def owner_required(f):
    """
    イベントオーナーかどうかをチェック
    オーナーじゃない場合は、 403 Forbidden を返す

    @event_view と @account_required は必須
    """
    def _wrapped(request, event, *args, **kwargs):
        if request.account != event.user:
            # TODO: Forbidden Page
            return HttpResponseForbidden()
        return f(request, event, *args, **kwargs)
    return _wrapped
