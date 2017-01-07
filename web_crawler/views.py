from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver

# Create your views here.
def index(request):
    return render(request, 'web_crawler/index.html')

def crawling(request):
  return render(request,'web_crawler/crawling_result.html')
