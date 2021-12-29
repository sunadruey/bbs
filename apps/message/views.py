from django.shortcuts import render

# Create your views here.

from .models import UserMessage


def getform(request):
    # 返回全部数据局
    # all_message=UserMessage.objects.all()

    # 筛选查询
    # all_message = UserMessage.objects.filter(name='bobby',address='北京市朝阳区')
    # for message in all_message:
    #     print(message.name)

    # 保存数据到数据库中
    # user_message=UserMessage()
    # user_message.name="赵丽颖"
    # user_message.message="赵丽颖离婚了"
    # user_message.address="河北省廊坊市"
    # user_message.email="zhaoliying@163.com"
    # user_message.object_id="2"
    # user_message.save()

    # 数据库的删除操作

        # 删除queryset全部
        # all_message=UserMessage.objects.all()
        # all_message.delete()

        # 删除单条
        # all_message=UserMessage.objects.filter(name='crm')
        # for message in all_message:
        #     message.delete()
        #     # print(message.name)



    # # 前端提交保存到数据库
    # if request.method=="POST":
        #    name = request.POST.get('name','')
        #    message = request.POST.get('message', '')
        #    address=request.POST.get('address', '')
        #    email= request.POST.get('email', '')
        #
        #    user_message = UserMessage()
        #    user_message.name=name
        #    user_message.message=message
        #    user_message.address=address
        #    user_message.email=email
        #    user_message.object_id="3"
        #    user_message.save()

        # 数据库反向显示到html页面
    message=None
    all_message = UserMessage.objects.filter(name='赵丽颖')
    if all_message:
        message=all_message[0]


        return  render(request, 'messageform.html',{
            "my_message":message
        })

