# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.db.models import *
from django.db import connection
from django.template import RequestContext
import datetime
from models import *

def thanks(request):
     return render_to_response('fulltext.html')
    

def post_comment(request):
       
    c = comment()
    c.article_id = '%s'% request.POST['article_id']
    c.name = '%s' % request.POST['nickname']
    c.opinion= '%s' % request.POST['comment']
    
    feed = "Спасибо за ваш отзыв, он будет опубликован после проверки модератором."

    c.save()

    return render_to_response('thanks.html',{'feed' : feed} )


def fulltext(request): #вывод выбранной статьи
    c = {}
    c.update(csrf(request))
    
    art_id = '%s' % request.GET['article_id']
    name = '%s' % request.GET['name']
    desc = '%s' % request.GET['desc']

    #curr_art = dobase.objects.get(id=art_id)

    comm_set = comment.objects.filter(article_id = art_id, checked = 'True' )
    if (comm_set == comment.objects.none()):
        return render_to_response('fulltext.html', {'desc': desc,'name': name, 'article_id': art_id }, context_instance=RequestContext(request))
    else:
        return render_to_response('fulltext.html', {'desc': desc,'name': name, 'article_id': art_id, 'comm_set' : comm_set }, context_instance=RequestContext(request))


    
def index(request):
    cursor = connection.cursor()
        
    preview=[]
    items = dobase.objects.all()
    for article in items:
        article.preview = article.description[:301]+'...'
        cursor.execute( 'SELECT Count(id) FROM core_comment WHERE article_id = %s and checked = 1', [int(article.id)] )
        article.num_comm = int(cursor.fetchone()[0])
        
    paginator = Paginator(items, 10) # Show contacts per page

    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    
    return render_to_response('index.html', {'items': items })

def hello(request):
    return HttpResponse("Hello worldsss")

def cur_time(request):
    now = datetime.datetime.now()
    html ='<html><body> Сейчас %s .</body><html>'% now
    return HttpResponse(html)
