import urllib2
web=urllib2.urlopen("https://www.youtube.com")
print "result code "+str(web.getcode())
data=web.read()
print data