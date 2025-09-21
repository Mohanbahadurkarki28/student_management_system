# from django.http import HttpResponse
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Notification

# # Create your views here.

# def index(request):
#     return render(request, "authentication/login.html")

# def dashboard(request):
#     unread_notification = Notification.objects.filter(user=request.user, is_read=False)
#     unread_notification_count = unread_notification.count()
#     return render(request, "students/student-dashboard.html")



# def mark_notification_as_read(request):
#     if request.method == 'POST':
#         notification = Notification.objects.filter(user=request.user, is_read=False)
#         notification.update(is_read=True)
#         return JsonResponse({'status': 'success'})
#     return HttpResponse()

# def clear_all_notification(request):
#     if request.method == "POST":
#         notification = Notification.objects.filter(user=request.user)
#         notification.delete()
#         return JsonResponse({'status': 'success'})
#     return HttpResponse()


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

def index(request):
    return render(request, "authentication/login.html")

@login_required
def dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "students/student-dashboard.html", {
        'unread_notifications': unread_notification,
        'unread_count': unread_notification_count
    })


@login_required
def mark_notification_as_read(request, notification_id=None):
    if request.method == 'POST':
        if notification_id:  # mark a specific one
            Notification.objects.filter(user=request.user, id=notification_id).update(is_read=True)
        else:  # mark all as read
            Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponse(status=405)  # method not allowed


@login_required
def clear_all_notification(request):
    if request.method == "POST":
        Notification.objects.filter(user=request.user).delete()
        return JsonResponse({'status': 'success'})
    return HttpResponse(status=405)
