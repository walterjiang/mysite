#coding:utf-8
from django.conf import settings
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class om_order(models.Model):
    order_id=models.IntegerField(blank=False,db_index=True,help_text='order id')
    order_no = models.CharField(blank=False,db_index=True,max_length=25,help_text='订单编号')
    order_type=models.IntegerField(help_text='订单类型 1:代购|2:自助购')
    total_count =models.IntegerField(help_text='订单总数量,由订单详情表数量累计而得')
    total_amount = models.IntegerField(help_text='订单总金额,由订单详情表金额累计而得')
    total_freight = models.IntegerField(help_text='订单总运费,由订单详情表运费累计而得')
    order_time = models.DateTimeField(help_text='下单时间',db_index=True)
    order_status=models.IntegerField(help_text='订单状态',db_index=True)
    order_remark=models.CharField(max_length=500,help_text='订单备注')
    seller_id = models.IntegerField(help_text='卖点id')
    seller_name = models.CharField(help_text='卖家名字',max_length=50)
    user_id =models.IntegerField(help_text='用户id',db_index=True)
    user_name=models.CharField(help_text='用户名',max_length=20)
    purchaser_id=models.IntegerField(help_text='采购id')
    purchaser_name = models.CharField(max_length=20,help_text='采购用户名')
    order_source = models.IntegerField(help_text='订单来源,1:C端用户,2:B端用户')
    cancel_type=models.IntegerField(help_text='订单取消类型， 1:用户取消，2:系统取消')
    cancel_reason = models.CharField(max_length=200,help_text='订单取消原因')
    shop_source = models.CharField(max_length=20,help_text='店铺来源， 例如TM、TB、JD等')
    shop_id =models.IntegerField(help_text='店铺id')
    shop_nick = models.CharField(max_length=50,help_text='店铺名称')
    shop_link = models.CharField(max_length=100,help_text='店铺url')
    platform=models.IntegerField(help_text='订单创建平台 1pc 2ios 3android 4代购助手(目前只支持chrome)')
    language = models.IntegerField(help_text='用户下单语言')
    promotion_id = models.IntegerField(help_text='促销id')
    receive_type = models.IntegerField(help_text='接单类型 1:普通|2:特定金额|3:特殊用户|4:特殊店铺|5:未知平台|6:yupoo|7:1688')
    urgent=models.IntegerField(help_text='是否加急订单')
    pay_time=models.DateTimeField(help_text='支付时间',db_index=True)
    delivery_id = models.IntegerField(help_text='运送方式id')
    delivery_name = models.CharField(max_length=20,help_text='运送方式名')
    express_no = models.CharField(max_length=45,help_text='发货快递号')
    country = models.CharField(max_length=32, help_text='配送目的国家')
    state=models.CharField(max_length=150,help_text='收货地址的州')
    city = models.CharField(max_length=150,help_text='城市名称')
    address=models.CharField(max_length=500,help_text='街道地址')
    consignee =models.CharField(max_length=100,help_text='收货人名')
    phone = models.CharField(max_length=100,help_text='收货人电话')
    warehouse_id= models.IntegerField(help_text='仓库id')

class um_user(models.Model):
    user_id=models.IntegerField(help_text='用户id',blank=False,db_index=True)
    user_name=models.CharField(max_length=20,help_text='用户名称')
    reality_money=models.FloatField(help_text='可提款的金额,用户充值的金额')
    virtual_money = models.FloatField(help_text='奖励金额,返款,不可提款')
    freeze_money = models.FloatField(help_text='冻结金额,不可使用')
    point = models.IntegerField(help_text='积分')
    reg_ip = models.IntegerField(help_text='注册ip')
    reg_location=models.CharField(max_length=40,help_text='注册国家来源')
    reg_time=models.DateTimeField(help_text='注册时间')
    last_login_time=models.DateTimeField(help_text='上次登录时间')
    last_login_ip=models.IntegerField(help_text='上次登录ip')
    reg_tag=models.CharField(max_length=25,help_text='注册渠道跟踪参数')
    reg_country_code=models.CharField(max_length=4,help_text='注册国家编码')
    reg_from=models.CharField(max_length=25,help_text='注册来源')
    reg_platform=models.IntegerField(help_text='注册的终端：1pc，2ios，3android...')
    language=models.IntegerField(help_text='语言')
    email=models.CharField(max_length=100,help_text='邮箱')
    is_valid=models.IntegerField(help_text='邮箱是否验证')
    is_pro_account=models.IntegerField(help_text='是否付费会员')
    sensitive_goods_user=models.IntegerField(help_text='是否敏感品用户')
    warehouse_id=models.IntegerField(help_text='仓库id，1:深圳仓，2:香港仓，3:scb仓')
    birthday=models.CharField(max_length=32,help_text='生日')
    gender=models.IntegerField(help_text='性别')
    growth=models.IntegerField(help_text='成长值')
    first_shopping=models.IntegerField(help_text='是否第一次购物')
    first_send = models.IntegerField(help_text='是否第一次寄送包裹')
    first_show=models.IntegerField(help_text='是否第一次晒单')

class custom_sql(models.Model):
    user = models.ForeignKey(User, verbose_name="更新者", editable=False)
    sql_name = models.CharField(max_length=100,help_text='查询名称',unique=True,verbose_name='查询名称')
    sql_conten=models.TextField(help_text='查询语句',max_length=1500,verbose_name='SQL模板')
    sql_para = models.TextField(help_text='查询参数',max_length=5000,blank=True,verbose_name='参数集')
    sql_remark = models.TextField(help_text='查询备注说明',blank=True,verbose_name='备注说明')
    creat_time=models.DateTimeField(help_text='创建时间',auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(help_text='更新时间',auto_now=True,validators='更新时间')

class SqlAdmin(admin.ModelAdmin):
    list_display = ['sql_name','sql_conten','sql_para','sql_remark','creat_time','update_time','user']

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user = request.user
        obj.save()

admin.site.register(om_order)
admin.site.register(um_user)
admin.site.register(custom_sql,SqlAdmin)