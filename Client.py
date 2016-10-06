import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000')
print 'login', server.login('qq', 'ww', 'host')
print 'logout', server.logout('user')
print 'discovery', server.discovery('user')
print 'unidir', server.unidir('user')
print 'set_attribute', server.set_attribute('user')
print 'get_attribute', server.get_attribute('user')