from dialogmail import DialogMail
from django.conf import settings


def use_dm(f):
    def wrapper(*args, **kwargs):
        dm = DialogMail(settings.DIALOGMAIL_RPC_URI,
                        settings.DIALOGMAIL_SECRET)
        return f(dm, *args, **kwargs)
    return wrapper


@use_dm
def dialogmail_find_user(dm, email):
    results = dm.list_user_search(email)
    for result in results:
        if result['email'] == email:
            return result['id']
    return None


@use_dm
def dialogmail_subscribe(dm, email):
    uid = dialogmail_find_user(email)

    if not uid:
        uid = dm.create_user({'email': email})

    dm.update_user_groups(uid, [{
        'group': settings.DIALOGMAIL_GROUP_ID,
        'status': 1,
        'flag': 1}])


@use_dm
def dialogmail_unsubscribe(dm, email):
    uid = dialogmail_find_user(email)
    if uid:
        dm.delete_user(uid)
