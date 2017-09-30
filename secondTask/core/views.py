# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

def helloworld(request, name=None):
    return  render(request,'base.html',{'name':name})
    #return HttpResponse("Hello!"+variable)

def blogList(request, name=None):
    return  render(request,'bloglist.html',{'name':name})

def postList(request, name=None):
    return  render(request,'postlist.html',{'name':name})

def singlePost(request, name=None):
    return  render(request,'post.html',{'name':name})

def userProfile(request, name=None):
    return  render(request,'userprofile.html',{'name':name})


# Create your views here.
