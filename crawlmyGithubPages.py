# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Automatically Create an Overview-Website out of 'User' Github Repos

# <codecell>

import requests
import json
import os

# <codecell>

username = 'balzer82'

# <codecell>

r = requests.get('https://api.github.com/users/%s/repos' % username)

# <codecell>

repos=[]
desc=[]
url=[]
for i in range(1,len(r.json())):
    repos.append(r.json()[i]['name'])
    desc.append(r.json()[i]['description'])
    url.append(r.json()[i]['html_url'])
    
    # Check if there is a Github Page
    # If yes, take this url instead of the Repository URL
    b = requests.get('https://api.github.com/repos/%s/%s/branches' % (username, repos[-1]))
    for j in range(len(b.json())):
        if b.json()[j]['name']=='gh-pages':
            url[-1] = 'http://balzer82.github.io/%s' % repos[-1]

# <codecell>


# <headingcell level=2>

# Write index.html

# <codecell>

f=open('index.html','w')

prestring="""
<html>
<head>
<link rel="stylesheet" href="style.css">

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-46744695-1', 'auto');
  ga('send', 'pageview');

</script>

</head>
<body>

<h1>balzer82.github.io</h1>
    <div>
    <h2>Repositories</h2>
        <ul>
"""
f.write(prestring)

for i in range(len(repos)):
    f.write('\t\t\t\t<li><img src="%s">\n' % 'github.png')
    f.write('\t\t\t\t<h3><a href=\'%s\'>%s</a></h3>\n' % (url[i], repos[i]))
    f.write('\t\t\t\t<p>%s</p></li>\n' % desc[i].encode('utf-8'))

    
    
poststring ="""
        </ul>
    </div>
    <p>Background Image CC BY-NC-ND 2.0 von Flickr mr. Wood</p>
    <p>Github Logo by Github User JD Pirtle</p>
</body>
</html>
"""
f.write(poststring)
f.close()

# <codecell>

print('Done.')

