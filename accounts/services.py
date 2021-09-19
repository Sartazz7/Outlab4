import requests
from .models import Profile , Repository
from datetime import datetime

def present_profile(p):
    for profile in Profile.objects.all():
        if(p.user.username == profile.user.username):
            return True
    return False

def search_profile(user_id):
    for profile in Profile.objects.all():
        if(user_id == profile.user_id):
            return profile

def fetch(user_id):
    p = Profile()
    p.user = user_id
    if(present_profile(p)):
        return Profile.objects.all()
    
    try:
        r = requests.get('https://api.github.com/users/'+user_id.username)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    data = r.json()
    p.followers = data["followers"]
    p.last_update = datetime.now()
    p.save()
    
    try:
        res = requests.get('https://api.github.com/users/'+user_id.username+'/repos')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    repos = res.json()
    for repo in repos:
        r = Repository()
        r.name = repo["name"]
        r.star = repo["stargazers_count"]
        r.save()
        r.user_name.set([p])
        r.save()
    
    return Profile.objects.all()

def get_star(repo):
    return repo.stars

def User_data(id):
    profile = None
    for p in Profile.objects.all():
        if(p.user_id == id):
            profile = p
            break
    R = profile.repository_set.all()
    R = list(R)
    R.sort(key=get_star, reverse=True)
    return R

def update(id, user):
    if (user.id != id):
        return False
    profile = None
    for p in Profile.objects.all():
        if(p.user_id == id):
            profile = p
            break
    profile.delete()
    fetch(user)
    return True