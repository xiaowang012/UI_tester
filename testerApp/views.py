#coding=utf-8
from django.shortcuts import render,redirect
from django.contrib import auth
from . import forms

# Create your views here.
# 127.0.0.1:5000 (仅输入IP+PORT) 判断是否在登录状态
def host(request):
    if request.session.get('is_login',None) == True:
        return redirect('/my_testcase/')
    else:
        return redirect('/login/')
    
#用户登录
def login(request):
    # if request.session.get('is_login',None) == True:
        # return redirect('/management/')
    if request.method == "GET":
        form = forms.UserForm
        return render(request, "login.html",{"form":form})
    elif request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            #authenticate
            login_user_obj = auth.authenticate(username = username, password = password)
            if not login_user_obj:
                #定义密码错误信息
                dic1 = {}
                dic1['message'] = '用户名或密码错误!'
                return render(request, "login.html", {"form": form,"dic1":dic1})
            else:
                request.session["is_login"] = True
                auth.login(request,login_user_obj)
                return redirect('/home/')
                
        else:
            return render(request, "login.html", {"form": form})

#用户注册
def register(request):
    if request.method == "GET":
        form = forms.RegisterForm
        return render(request, "register.html",{"form":form})
    elif request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            #创建用户
            if password == password1:
                if not User.objects.filter(username = str(username)).first():
                    #用户名查重,如果查不到，正常创建用户
                    try:
                        User.objects.create_user(username = str(username),password = str(password))
                    except:
                        #返回对应的错误提示信息到页面
                        message = ' 注册: ' + str(username) +' Failed!'
                        dic2 = {'frame_type':'alert alert-dismissable alert-danger','title':'ERROR ','message':message}
                        return render(request,'register.html',{'form':form,'dic2':dic2})
                    else:
                        #返回对应的注册成功提示信息到页面
                        message = ' 注册: ' + str(username) +' SUCCESS!'
                        dic2 = {'frame_type':'alert alert-success alert-dismissable','title':'SUCCESS ','message':message}
                        return render(request,'register.html',{'form':form,'dic2':dic2})
                else:
                    error = '用户: '+ str(username) + ' 已存在! 请不要重复注册!'
                    return render(request, "register.html", {"form": form,"error":error})
            else:
                error_msg = '两次输入的密码不一致!'
                return render(request, "register.html", {"form": form,"error":error_msg})
        else:
            #print(form.errors)
            #未通过表单验证
            clear_err = form.errors.get('__all__')
            #print(clear_err)
            if clear_err:
                clear_err = str(clear_err).replace('<ul class="errorlist nonfield"><li>','').replace('</li></ul>','')
            return render(request, "register.html", {"form": form,'clear_err':clear_err})
            
#用户登出
#@login_required
#@permission_check
def logout(request):
    auth.logout(request)
    return redirect('/login/')

#我的测试用例页面
# @login_required
# @permission_check
def my_testcase(request):
    if request.method == 'GET':
        #查询测试用例数据
        form = None
        #获取当前用户名
        username = request.user
        #前端数据
        dic1 = {'username':username,'active1':'active','active2':'','active3':'',\
        'active4':'','active5':'','current_page_number':1}
        #查看测试用例数据(一次10条)
        # testcase_info = models.Books.objects.all()[:5]
        # #加入每一行数据的的样式到queryset中
        # for data in book_info:
        #     data.style = random.choice(['success','info','warning','error'])
        # return render(request,'my_testcase.html',{'form':form,'list1':book_info,'dic1':dic1})
        return render(request,'my_testcase.html')
