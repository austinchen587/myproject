from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    # 定义多选项
    NEEDS_CHOICES = [
        ('有知识付费意识', '有知识付费意识'),
        ('排斥培训', '排斥培训'),
        ('被培训机构骗过', '被培训机构骗过'),
        ('表示工作难找', '表示工作难找'),
        ('找工作有多久', '找工作有多久'),
        ('想尽快就业', '想尽快就业'),
        ('想转行', '想转行'),
        ('了解过云计算', '了解过云计算'),
        ('认可云计算', '认可云计算'),
    ]

    PERSONALITY_CHOICES = [
        ('犹豫', '犹豫'), ('理性', '理性'), ('妈宝男', '妈宝男'),
        ('怕吃苦', '怕吃苦'), ('墨迹', '墨迹'), ('迷茫', '迷茫'),
        ('攻击性大', '攻击性大'), ('自我内耗', '自我内耗'),
    ]

    PROMOTION_CHOICES = [
        ('云计算小视频+文字概述', '云计算小视频+文字概述'),
        ('云计算的服务模式', '云计算的服务模式'),
        ('云计算的薪资和发展空间', '云计算的薪资和发展空间'),
        ('云计算岗位及内容', '云计算岗位及内容'),
        ('云计算与数字经济', '云计算与数字经济'),
        ('行业介绍', '行业介绍'),
        ('政策推进趋势', '政策推进趋势'),
    ]

    # 使用多选复选框字段
    customer_needs_analysis = forms.MultipleChoiceField(
        choices=NEEDS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    customer_personality_analysis = forms.MultipleChoiceField(
        choices=PERSONALITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cloud_computing_promotion_content = forms.MultipleChoiceField(
        choices=PROMOTION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Customer
        exclude = ['created_by', 'updated_by']  # 排除自动设置的字段

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        # 设置所有字段为非必填
        for field in self.fields.values():
            field.required = False

        # 设置默认值，确保 JSONField 可以处理 None 值
        if 'instance' in kwargs and kwargs['instance']:
            instance = kwargs['instance']
            self.fields['customer_needs_analysis'].initial = instance.customer_needs_analysis or []
            self.fields['customer_personality_analysis'].initial = instance.customer_personality_analysis or []
            self.fields['cloud_computing_promotion_content'].initial = instance.cloud_computing_promotion_content or []

    def save(self, commit=True):
        # 获取表单实例
        instance = super(CustomerForm, self).save(commit=False)

        # 保存多选字段为 JSON 格式
        instance.customer_needs_analysis = self.cleaned_data['customer_needs_analysis']
        instance.customer_personality_analysis = self.cleaned_data['customer_personality_analysis']
        instance.cloud_computing_promotion_content = self.cleaned_data['cloud_computing_promotion_content']

        # 提交保存
        if commit:
            instance.save()
        return instance