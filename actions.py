from django.http import HttpResponse
from django.http import StreamingHttpResponse
import os
from django.shortcuts import render
import time
from datetime import datetime
import pytz
import random
import sqlite3

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
        dir=a+'/'+b
        try:
            f=open(dir,'rb')
            print(dir)
            f.close()
            if a=='pic':
                f=open(dir,'rb')
                r=f.read()
                f.close()
                return HttpResponse(r)
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


def getSignup(req):
    try:
        usrname=req.POST['usrname']
        passwd=req.POST['passwd']
        con=sqlite3.connect('t1.db')
        print('1')
        try:
            con.execute('create table usr1 (usrname,passwd)')
            print('2')

        finally:
            print('3')
            var=con.execute('select usrname from usr1 where usrname="{usrname}"'.format(usrname=usrname))
            sel=var.fetchone()
            print('4')
            try:
                if(sel[0]==usrname):
                    con.close()
                    return HttpResponse('该用户已存在！')
                else:
                    con.close()
                    return HttpResponse('Something Wrong!')
            except:
                print('5')
                con.execute('insert into usr1 values ("{usrname}","{passwd}")'.format(usrname=usrname,passwd=passwd))
                print('6')
                con.commit()
                con.close()
                return HttpResponse('注册成功！')

    except:
        return HttpResponse('Something Wrong!')
        
def getSignin(req):
    try:
        cpasswd=req.POST['cpasswd']
        zone8='Asia/Shanghai'
        zo8=pytz.timezone(zone8)
        tiz8=datetime.fromtimestamp(time.time(),zo8)
        wekd=tiz8.weekday()
        if(cpasswd!=str(wekd)):
            return HttpResponse('验证出错！')
        usrname=req.POST['usrname']
        passwd=req.POST['passwd']
        con=sqlite3.connect('t1.db')
        var=con.execute('select passwd from usr1 where usrname="{usrname}"'.format(usrname=usrname))
        sel=var.fetchone()
        try:
            if(sel[0]==passwd):
                con.close()
                return HttpResponse('登入成功！')
            else:
                return HttpResponse('密码错误！')
        except:
            return HttpResponse('用户不存在！')
    except:
        return HttpResponse('Something Wrong!')
