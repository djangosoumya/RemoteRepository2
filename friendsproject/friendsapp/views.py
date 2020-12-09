from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from.models import FriendsData

def add_friends(request):
    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        location = request.POST.get('loc')

        data = FriendsData(
            first_name=fname,
            last_name=lname,
            mobile=mobile,
            email = email,
            gender=gender,
            location=location
        )
        data.save()
        friends = FriendsData.objects.all()
        return render(request,'add_friends.html',{'soumya':friends})
    else:
        friends = FriendsData.objects.all()
        return render(request,'add_friends.html',{'soumya':friends})

#def display_friends(request):
 #   friends = FriendsData.objects.all()
 #   return render(request,'add_friends.html',{'soumya':friends})

def update_friends(request,id):
    friend = FriendsData.objects.get (id=id)
    return render(request,'update_friends.html',{'friends':friend})

def update_friends_save(request,id):
    friend = FriendsData.objects.get(id=id)
    friend.first_name = request.POST.get('fname')
    friend.last_name = request.POST.get('lname')
    friend.mobile = request.POST.get('mobile')
    friend.email = request.POST.get('email')
    friend.gender = request.POST.get('gender')
    friend.location = request.POST.get('loc')
    friend.save()
    return redirect('/')


def delete_friends(request,id):
    friend = FriendsData.objects.get(id=id)
    # if request.method == 'POST':
    friend.delete()
    return redirect('/')
    return render(request,'add_friends.html')



