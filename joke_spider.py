# -*- coding: UTF-8 -*-
import urllib2

from bs4 import BeautifulSoup

url = "http://www.qiushibaike.com/"
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response = urllib2.urlopen(request)
print response.getcode()

html_cont = response.read()
soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
jokes = soup.find_all('div', class_="content")

count = 1
for joke in jokes:
    print 'joke  %d: %s' % (count, joke.get_text())
    count = count + 1

#以html打印出来
fout = open('output2.html', 'w')
fout.write("<html>")
fout.write("<body>")
fout.write("<table>")
fout.write("<tr>Just for fun</tr>")
count2 = 1
for joke in jokes:
    fout.write("<tr>")

    fout.write("<td>%d : %s</td>" % (count2,joke.get_text().encode('gbk')))
    fout.write("</tr>")
    count2 = count2 + 1
fout.write("</table>")
fout.write("</body>")
fout.write("</html>")
