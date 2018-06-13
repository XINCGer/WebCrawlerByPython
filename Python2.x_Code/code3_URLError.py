#coding:utf-8

import urllib2

# 捕获URL异常
# request = urllib2.Request('http://www.abc.com')
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError, e:
#     print e.reason

# HTTP状态码
# 100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
# 101： 转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
# 102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
# 200：请求成功      处理方式：获得响应的内容，进行处理
# 201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到
# 202：请求被接受，但处理尚未完成    处理方式：阻塞等待
# 204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
# 300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
# 301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
# 302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL
# 304：请求的资源未更新     处理方式：丢弃
# 400：非法请求     处理方式：丢弃
# 401：未授权     处理方式：丢弃
# 403：禁止     处理方式：丢弃
# 404：没有找到     处理方式：丢弃
# 500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
# 501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
# 502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
# 503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。

# HTTP异常捕获
# req = urllib2.Request('http://blog.csdn.net/cqcre1')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print e.code
#     print e.reason

# 区分HTTP父子类异常捕获
# req = urllib2.Request('http://blog.csdn.net/cqcre1')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print e.code
# except urllib2.URLError, e:
#     print e.reason
# else:
#     print "OK"

# 加入 hasattr属性提前对属性进行判断
req = urllib2.Request('http://blog.csdn.net/cqcre1')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"


