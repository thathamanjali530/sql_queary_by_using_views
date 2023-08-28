from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.

def display_topic(request):
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.all().order_by('topic_name')
    QSTO=Topic.objects.all().order_by('-topic_name')
    QSTO=Topic.objects.filter(topic_name='cricket').order_by('topic_name')
    QSTO=Topic.objects.exclude(topic_name='kabaddi').order_by('topic_name')
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.all().order_by(Length('topic_name'))
    QSTO=Topic.objects.all().order_by(Length('topic_name').desc())
    QSTO=Topic.objects.all()[2:4:]
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def dispaly_webpage(request):
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.filter(name='Anjali').order_by('name')
    QSWO=Webpage.objects.exclude(name='Anjali').order_by('name')
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.all().order_by(Length('name'))
    QSWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'QSWO':QSWO}
    return render(request,'dispaly_webpage.html',d)

def display_AccessRecord(request):
    QSAO=AccessRecord.objects.all()
    QSAO=AccessRecord.objects.all().order_by('-author')
    QSAO=AccessRecord.objects.all().order_by('author')
    QSAO=AccessRecord.objects.filter(author='Tulasi').order_by('author')
    QSAO=AccessRecord.objects.exclude(author='Tulasi').order_by('author')
    QSAO=AccessRecord.objects.all()
    QSAO=AccessRecord.objects.all().order_by(Length('author'))
    QSAO=AccessRecord.objects.all().order_by(Length('author').desc())

    d={'QSAO':QSAO}
    return render(request,'display_AccessRecord.html',d)

def insert_topic(request):
    tn=input('enter topic_name:')
    TO=Topic.objects.get_or_create(topic_name=tn)
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn=input('enter topic_name:')
    n=input('enter name:')
    u=input('enter u:')
    To=Topic.objects.get(topic_name=tn)

    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=u)[0]
    Wo.save()

    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'dispaly_webpage.html',d)

def insert_access(request):
    
    pk=input('enter name:')
    d=input('enter date:')
    a=input('enter author:')
    Wo=Webpage.objects.get(pk=pk)
    

    Ao=AccessRecord.objects.get_or_create(pk=Wo,date=d,author=a)[0]
    Ao.save()

    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_AccessRecord.html',d)



