from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
import random
import smtplib
import email.message
# Create your views here.
def Login(request):
    if request.POST:
        em = request.POST['em']
        ps = request.POST['ps']
        
        try:
            valid = CreateAccount.objects.get(email=em)
            if valid.password == ps:
                request.session['userid'] = valid.id
                return redirect('index')
            else:
                return HttpResponse("<a href=''> Wrong Password </a>")
        except:
            return HttpResponse("<a href=''> Email Id Not Found </a>")
    return render(request,'t_login.html')
def Sinup(request):
    if request.POST:
        un = request.POST['un']
        em = request.POST['em']
        ph = request.POST['ph']
        ps = request.POST['ps']
        cps = request.POST['cps']
        
        try:
            valid = CreateAccount.objects.get(email=em)
            return HttpResponse("<a href='' style = 'color:red'>Sorry Email Already Registerd.....</a>")
        except:
            if cps == ps:
                obj = CreateAccount()
                obj.username = un 
                obj.M_no = ph
                obj.email = em
                obj.password = cps
                obj.save()
            else:
                return HttpResponse("<a href='' style='color:red'>Passwords Are Not carrect......</a>")
        return redirect('login')
    return render(request,'t_sinup.html')
def Home(r):
    return render(r,'home.html')
def Forget_ps(r):
    if r.POST:
        em1 = r.POST['em1']
        
        try:
            valid = CreateAccount.objects.get(email=em1)

            sender_email = "info.tritech.program@gmail.com"
            sender_pass = "Jenish@1213"
            receiver_email = em1
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            
            # OTP Create ----------------
            nos = [1,2,3,4,5,6,7,8,9]
            otp = ""
            for i in range(4):
                otp += str(random.choice(nos))
                print(otp)
            
            your_message = f"""
            This Is Your OTP
            {otp}
            
            
            Don't Share With Others....
            """
            
            msg = email.message.Message()
            msg['Subject'] = "OTP From This Site"
            msg['From'] = sender_email
            msg['To'] = receiver_email
            password = sender_pass
            msg.add_header('Content-Type','text/html')
            msg.set_payload(your_message)

            server.starttls()
            server.login(msg['From'],password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            
            r.session['otp'] = otp
            
            r.session['New_User_data'] = valid.id
            
            return redirect('C_otp')
            
        except:
            return HttpResponse("<a href=''> Email Id Not Found </a>")
    return render(r,'forg.html')

def C_otp(r):
    if 'otp' in r.session.keys():
        if r.POST:
            otp = r.POST['otp']
            if otp == r.session['otp']:
                print("OTP Is Match ....")
                del r.session['otp']
                return redirect("New_pass")
            else:
                del r.session['otp']
                return redirect('Forget_ps')
        return render(r,'otp.html')
    else:
        return redirect('login')

def New_pass(r):
    if 'New_User_data' in r.session.keys():
        if r.POST:
            ps = r.POST['ps']
            cps = r.POST['cps']
            
            if ps == cps:
                valid = CreateAccount.objects.get(id=int(r.session['New_User_data']))
                valid.password = cps
                valid.save()
                del r.session['New_User_data']
                return redirect('login')
            else:
                return redirect("New_pass")
        return render(r,'newpass.html')
    else:
        return redirect('ogin')