#!/usr/bin/python

from mod_pywebsocket import msgutil

def web_socket_do_extra_handshake(request):
    print('echo-cookie_wsh.py, web_socket_do_extra_handshake')
    print(request.headers_in.get('Cookie'))
    request.ws_cookie = request.headers_in.get('Cookie')

def web_socket_transfer_data(request):
    print('echo-cookie_wsh.py, web_socket_transfer_data')
    if request.ws_cookie is not None:
        print('request.ws_cookie is not None, sending %s' % request.ws_cookie)
        msgutil.send_message(request, request.ws_cookie)
    else:
        print('request.ws_cookie is None, sending (none)')
        msgutil.send_message(request, '(none)')
