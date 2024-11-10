# utils.py
def calculate_completion_rate(customer):
    # 定义模型字段并初始化已填写的字段数
    fields = [
        'phone', 'student_batch', 'is_invited', 'is_wechat_added', 'is_joined',
        'name', 'education', 'city', 'intention', 'customer_needs_analysis',
        'customer_personality_analysis', 'cloud_computing_promotion_content',
        'is_closed', 'is_contacted', 'data_source', 'wechat_name', 
        'attended_first_live', 'attended_second_live', 'first_day_watch_duration',
        'second_day_watch_duration', 'first_day_feedback', 'second_day_feedback',
        'persona_chat', 'additional_students', 'comments_count', 
        'deal_7_days_checked', 'deal_7_days_text', 'deal_14_days_checked', 
        'deal_14_days_text', 'deal_21_days_checked', 'deal_21_days_text', 
        'is_course_reminder', 'description', 'supervisor_comments'
    ]
    total_fields = len(fields)
    filled_fields = sum(1 for field in fields if getattr(customer, field))

    return (filled_fields / total_fields) * 100  # 返回百分比