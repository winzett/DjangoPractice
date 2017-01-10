from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# Create your views here.
def index(request):
    return render(request, 'web_crawler/index.html')

def crawling(request):
  test_val = "python test in html file"
  driver = webdriver.PhantomJS()
  driver.set_window_size(1024, 768)
  driver.get('https://www.riskmap.com/#/latest')

  html_result = driver.page_source
  soup = BeautifulSoup(html_result, "html.parser")
  typing=soup.find_all("div",{"class":"centre"})


  return render(request, 'web_crawler/crawling_result.html', {'result':typing})
