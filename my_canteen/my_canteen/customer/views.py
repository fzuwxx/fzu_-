from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, UpdateForm  # 导入表单，下面将介绍
from django.contrib import messages
from .models import Customer


# Create your views here.
def register(request):
    register_form = RegisterForm()
    if request.session.get('is_login', None):  # 不允许重复登录
        return render(request, 'customer/index.html', locals())  # 自动跳转到首页
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            tel = register_form.cleaned_data['tel']

            if password1 != password2:  # 判断两次密码是否相同
                print("[DEBUG][POST][STATE]:两次输入的密码不同！")
                # message = "两次输入的密码不同！"
                return render(request, 'customer/register.html', locals())
            else:
                same_id_cus = Customer.objects.filter(customer_name=username)
                # same_id_mng = StoreManager.objects.filter(manager_name=username)
                if same_id_cus:  # 用户名唯一
                    message = '顾客用户名已经存在~请换一个'
                    return render(request, 'customer/register.html', locals())
                # 当一切都OK的情况下，创建新用户
                else:
                    new_cus = Customer.objects.create(customer_name=username, customer_tel=tel,
                                                      customer_password=password1)
                    new_cus.save()
                    # 自动跳转到登录页面
                    login_form = LoginForm()
                    message = "注册成功！"
                    return render(request, 'customer/login.html', locals())  # 自动跳转到登录页面
    else:
        return render(request, 'customer/register.html', locals())

    return render(request, 'customer/register.html', locals())


def login(request):
    login_form = LoginForm()
    if request.session.get('is_login', None):
        print("[DEBUG][POST][STATE]:已经登陆")
        return render(request, 'customer/index.html', locals())

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # identy 表示
            print("[DEBUG][POST][LOGIN][username]:{}".format(username))
            print("[DEBUG][POST][LOGIN][password]:{}".format(password))
            try:
                print("[DEBUG][POST][STATE]:查询顾客用户数据库")
                user_cus = Customer.objects.get(customer_name=username)
                if user_cus.customer_password == password:
                    print("[DEBUG][POST][USERNAME]:{}".format(user_cus.customer_name))
                    print("[DEBUG][POST][STATE]:登录成功")
                    messages.success(request, '{}登录成功！'.format(user_cus.customer_name))
                    user_cus.customer_status = 1
                    user_cus.save()
                    request.session['is_login'] = True
                    request.session['user_id'] = user_cus.customer_id
                    request.session['user_name'] = user_cus.customer_name
                    request.session['tel'] = user_cus.customer_tel
                    if user_cus.studentID is not None and user_cus.campus is not None:
                        request.session['studentID'] = user_cus.studentID
                        request.session['campus'] = user_cus.campus
                    return render(request, 'customer/index.html', locals())
                else:
                    messages.warning(request, '密码不正确，请重新输入！')
            except:
                messages.warning(request, '用户不存在，请注册！')
    return render(request, 'customer/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return render(request, 'customer/index.html', locals())
    user_id = request.session['user_id']
    print("[DEBUG][REQUEST][退出]]")
    print("[DEBUG][REQUEST][USER_ID]:{}".format(user_id))
    try:
        user = Customer.objects.get(customer_id=user_id)
        print("[DEBUG][REQUEST][退出]]：退出顾客身份")
        user.customer_status = 0  # 更新离线状态
        user.save()
    except:
        print("[DEBUG][request][STATE]:退出错误，无法更新数据库中用户状态")

    request.session.flush()
    return render(request, 'customer/index.html', locals())


def information(request):

    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    update_form = UpdateForm()
    user_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id=user_id).first()

    if customer.studentID and customer.campus:
        return redirect("customer:show_info")

    if request.method == "POST":
        update_form = UpdateForm(request.POST)
        if update_form.is_valid():
            new_studentID = update_form.cleaned_data['studentID']
            new_campus = update_form.cleaned_data['campus']
            try:
                # 更新Customer表中的学号和校区字段
                customer.studentID = new_studentID
                customer.campus = new_campus
                request.session['studentID'] = new_studentID
                request.session['campus'] = new_campus
                customer.save()

                messages.success(request, '学号和校区信息添加成功！')
                return render(request, 'customer/show_info.html', locals())
            except Exception as e:
                messages.warning(request, '学号和校区信息添加失败: {}'.format(str(e)))

    return render(request, 'customer/information.html', locals())


def show_info(request):
    return render(request, 'customer/show_info.html')
