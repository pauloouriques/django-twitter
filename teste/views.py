# -*- coding: cp1252 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

import urllib2
import tweepy

from models import Teste 

class Fields:
    key = ""
    secret = ""
    url = ""
    verifier = ""
    
global_auth = None
    
def index(request):
    tweets = Teste.objects.all()
    return render_to_response('teste/index.html', {'tweets': tweets,})
    
def tweets(request):
    fields = Fields()
    tws = request._get_raw_post_data()
    req = tws.split("&")
    fields.key = req[0].split("=")[1]
    fields.secret = req[1].split("=")[1]
    
    CONSUMER_KEY = fields.key
    CONSUMER_SECRET = fields.secret
    
    global global_auth
    global_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    fields.url = global_auth.get_authorization_url()

    return render_to_response('teste/tweets.html', {'fields': fields,})   

def mainPage(request):
    fields = Fields()
    text = request._get_raw_post_data()
    req = text.split("&")
    
    fields.verifier = req[0].split("=")[1]
    fields.key = req[1].split("=")[1]
    fields.secret = req[2].split("=")[1]

    global lobal_auth
    global_auth.get_access_token(fields.verifier)
    
    ACCESS_KEY = global_auth.access_token.key
    ACCESS_SECRET = global_auth.access_token.secret
    
    global_auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(global_auth)
    
    status  = []
    retorno = []
    
    status = api.home_timeline()
    for update in status:
        text = update.text
        splitedText = text.split(" ")
        
        if "#ambiente" in splitedText:
            retorno.append(update.user.screen_name)
            tweetText = "@" + update.user.screen_name +" usou a tag #ambiente. Parabens pela iniciativa."
            api.update_status(tweetText)
        
    return render_to_response('teste/mainPage.html', {'retweeteds': retorno,})
