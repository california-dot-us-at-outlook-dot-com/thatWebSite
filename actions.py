from django.http import HttpResponse
from django.http import StreamingHttpResponse
import os
from django.shortcuts import render
import time
from datetime import datetime
import pytz
import random
def sayHello(req):
    zone8='Asia/Shanghai'
    zo8=pytz.timezone(zone8)
    tiz8=datetime.fromtimestamp(time.time(),zo8)
    timeList={'year':tiz8.year,'mon':tiz8.month,'day':tiz8.day,'hour':tiz8.hour,'min':tiz8.minute,'zone':zone8}
    return render(req,'sayHello.html',timeList)

def say404(req):
    zone8='Asia/Shanghai'
    zo8=pytz.timezone(zone8)
    tiz8=datetime.fromtimestamp(time.time(),zo8)
    timeList={'year':tiz8.year,'mon':tiz8.month,'day':tiz8.day,'hour':tiz8.hour,'min':tiz8.minute,'zone':zone8}
    return render(req,'say404.html',timeList,status=404)

def sayHtml(req,a,b):
    if(a=='htmls' or a=='js' or a=='pic' or a=='css'):
        dir='./'+a+'/'+b
        try:
            open(dir,'rb')
            zone8='Asia/Shanghai'
            zo8=pytz.timezone(zone8)
            tiz8=datetime.fromtimestamp(time.time(),zo8)
            timeList={'year':tiz8.year,'mon':tiz8.month,'day':tiz8.day,'hour':tiz8.hour,'min':tiz8.minute,'zone':zone8}
            return render(req,b,timeList)
        except:
            return say404(req)
    else:
        return say404(req)

def getUpload(req):
    try:
        zone8='Asia/Shanghai'
        zo8=pytz.timezone(zone8)
        tiz8=datetime.fromtimestamp(time.time(),zo8)
        timeList={'year':tiz8.year,'mon':tiz8.month,'day':tiz8.day,'hour':tiz8.hour,'min':tiz8.minute,'zone':zone8}
    
        fp=req.FILES.get('uploadFile')
        dan='upload/'+str(timeList['year'])+'Y-'+str(timeList['mon'])+'M-'+str(timeList['day'])+'D-'+str(timeList['hour'])+'H-'+str(timeList['min'])+'m | '+fp.name
        try:
            f=open(dan,'rb')
            f.close()
            return render(req,"sayYesNo.html",{'SoF':'同名文件已存在！请稍后再试','jump':'/'})
        except:
            f=open(dan,'wb')
            for line in fp.chunks():
                f.write(line)
            f.close()
            return render(req,'sayYesNo.html',{'SoF':'上传成功！','jump':'sayUpload.html'})
    except:
        return render(req,"sayYesNo.html",{'SoF':'上传出错！','jump':'sayUpload.html'})