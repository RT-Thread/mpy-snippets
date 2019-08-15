
from microWebSrv import MicroWebSrv
import rtthread
import json
from machine import Pin, I2C
import fxos8700
import machine

# ----------------------------------------------------------------------------

@MicroWebSrv.route('/test')
def _httpHandlerTestGet(httpClient, httpResponse) :
    content = """\
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <meta charset="UTF-8" />
            <title>TEST GET</title>
        </head>
        <body>
            <h1>TEST GET</h1>
            Client IP address = %s
            <br />
            <form action="/test" method="post" accept-charset="ISO-8859-1">
                First name: <input type="text" name="firstname"><br />
                Last name: <input type="text" name="lastname"><br />
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """ % httpClient.GetIPAddr()
    httpResponse.WriteResponseOk( headers        = None,
                                  contentType    = "text/html",
                                  contentCharset = "UTF-8",
                                  content        = content )


@MicroWebSrv.route('/test', 'POST')
def _httpHandlerTestPost(httpClient, httpResponse) :
    formData  = httpClient.ReadRequestPostedFormData()
    firstname = formData["firstname"]
    lastname  = formData["lastname"]
    content   = """\
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <meta charset="UTF-8" />
            <title>TEST POST</title>
        </head>
        <body>
            <h1>TEST POST</h1>
            Firstname = %s<br />
            Lastname = %s<br />
        </body>
    </html>
    """ % ( MicroWebSrv.HTMLEscape(firstname),
            MicroWebSrv.HTMLEscape(lastname) )
    httpResponse.WriteResponseOk( headers        = None,
                                  contentType    = "text/html",
                                  contentCharset = "UTF-8",
                                  content        = content )

@MicroWebSrv.route('/sysdata')
def _httpHandlerTestGet(httpClient, httpResponse) :
    ax, ay, az = sensor.accelerometer
    mx, my, mz = sensor.magnetometer
    cpu_usage = machine.get_cpu_usage()
    cpu_value = cpu_usage[0] + cpu_usage[1] * 0.1
    ip = httpClient.GetIPAddr();
    
    content ={
        'status'      : 200,
        'body'        :{
        'status'      : 1,
        'result'      :{
            "versions":"3.0.3",
            "getTime":"1497594033",
            "cpuUtilization":cpu_value,
            "presentUtilization":1,
            "ipAddress": ip,
            "key":1,
            "Acceleration": {"accel_x" : ax, "accel_y" : ay, "accel_z" : az},
            "Magnetometer": { "mag_x"  : mx, "mag_y"   : my, "mag_z" :  mz}
        }
        }
            }
    headers = {
	    'Access-Control-Allow-Origin': '*',
	    'Access-Control-Allow-Methods': 'POST,GET',
	    'Access-Control-Allow-Headers': 'Content-Type, Authorization, Content-Length, X-Requested-With'
    }
    json_content = json.dumps(content)
    json_headers = json.dumps(headers)
    httpResponse.WriteResponseOk( headers        = headers,
                                  contentType    = "text/json",
                                  contentCharset = "UTF-8",
                                  content        = json_content)

@MicroWebSrv.route('/edit/<index>')             # <IP>/edit/123           ->   args['index']=123
@MicroWebSrv.route('/edit/<index>/abc/<foo>')   # <IP>/edit/123/abc/bar   ->   args['index']=123  args['foo']='bar'
@MicroWebSrv.route('/edit')                     # <IP>/edit               ->   args={}
def _httpHandlerEditWithArgs(httpClient, httpResponse, args={}) :
    content = """\
    <!DOCTYPE html>
    <html lang=en>
        <head>
            <meta charset="UTF-8" />
            <title>TEST EDIT</title>
        </head>
        <body>
    """
    content += "<h1>EDIT item with {} variable arguments</h1>"\
        .format(len(args))
    
    if 'index' in args :
        content += "<p>index = {}</p>".format(args['index'])
    
    if 'foo' in args :
        content += "<p>foo = {}</p>".format(args['foo'])
    
    content += """
        </body>
    </html>
    """
    httpResponse.WriteResponseOk( headers        = None,
                                  contentType    = "text/html",
                                  contentCharset = "UTF-8",
                                  content        = content )

# ----------------------------------------------------------------------------

def _acceptWebSocketCallback(webSocket, httpClient) :
    print("WS ACCEPT")
    webSocket.RecvTextCallback   = _recvTextCallback
    webSocket.RecvBinaryCallback = _recvBinaryCallback
    webSocket.ClosedCallback     = _closedCallback

def _recvTextCallback(webSocket, msg) :
    print("WS RECV TEXT : %s" % msg)
    webSocket.SendText("Reply for %s" % msg)

def _recvBinaryCallback(webSocket, data) :
    print("WS RECV DATA : %s" % data)

def _closedCallback(webSocket) :
    print("WS CLOSED")

# ----------------------------------------------------------------------------

#routeHandlers = [
#   ( "/test",  "GET",  _httpHandlerTestGet ),
#   ( "/test",  "POST", _httpHandlerTestPost )
#]

clk = Pin(('clk', 59), Pin.OUT_OD)
sda = Pin(('sda', 60), Pin.OUT_OD)
i2c = I2C(-1, clk, sda, freq=100000)
sensor = fxos8700.FXOS8700(i2c)

srv = MicroWebSrv(webPath='www/')
srv.MaxWebSocketRecvLen     = 256
srv.WebSocketThreaded       = False
srv.AcceptWebSocketCallback = _acceptWebSocketCallback
srv.Start(threaded=False)

# ----------------------------------------------------------------------------
