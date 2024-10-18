import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCustomerById } from '../api/customerApi';
import './CustomerDetail.css'; // 样式文件

const CustomerDetail = () => {
  const { id } = useParams();
  const [customer, setCustomer] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    loadCustomer();
  }, [id]);

  const loadCustomer = async () => {
    try {
      const data = await getCustomerById(id);
      setCustomer(data);
    } catch (error) {
      console.error('获取客户详情失败:', error);
    }
  };

  if (!customer) {
    return <p className="loading">正在加载客户信息...</p>;
  }

  return (
    <div className="customer-detail-wrapper">
      <h1 className="customer-detail-title">客户详情</h1>
      <div className="customer-detail-card">

        {/* 基本信息 */}
        <section>
          <h2>基本信息</h2>
          <p><strong>姓名：</strong> {customer.name || '未知'}</p>
          <p><strong>电话：</strong> {customer.phone}</p>
          <p><strong>学历：</strong> {customer.education}</p>
          <p><strong>专业类别：</strong> {customer.major_category}</p>
          <p><strong>状态：</strong> {customer.status}</p>
          <p><strong>当前所在城市：</strong> {customer.city}</p>
          <p><strong>学员期数：</strong> {customer.student_batch || '未指定'}</p> {/* 新增字段 */}
        </section>

        {/* 邀约及沟通 */}
        <section>
          <h2>邀约及沟通</h2>
          <p><strong>是否邀约：</strong> {customer.is_invited ? '是' : '否'}</p>
          <p><strong>沟通方式：</strong> {customer.communication_methods?.join(', ') || '无'}</p>
          <p><strong>是否加微信：</strong> {customer.is_wechat_added ? '是' : '否'}</p>
          <p><strong>客户微信名：</strong> {customer.wechat_name || '未填写'}</p>
          <p><strong>是否入群：</strong> {customer.is_joined ? '是' : '否'}</p>
        </section>

        {/* 挖需与性格分析 */}
        <section>
          <h2>挖需与性格分析</h2>
          <p><strong>客户挖需分析：</strong> {customer.customer_needs_analysis?.join(', ') || '无'}</p>
          <p><strong>客户性格分析：</strong> {customer.customer_personality_analysis?.join(', ') || '无'}</p>
          <p><strong>云计算推广内容：</strong> {customer.cloud_computing_promotion_content?.join(', ') || '无'}</p>
        </section>

        {/* 出勤及反馈 */}
        <section>
          <h2>出勤及反馈</h2>
          <p><strong>是否到课提醒：</strong> {customer.is_course_reminder ? '是' : '否'}</p>
          <p><strong>参加第一天直播：</strong> {customer.attended_first_live ? '是' : '否'}</p>
          <p><strong>第一天观看时长：</strong> {customer.first_day_watch_duration} 分钟</p>
          <p><strong>参加第二天直播：</strong> {customer.attended_second_live ? '是' : '否'}</p>
          <p><strong>第二天观看时长：</strong> {customer.second_day_watch_duration} 分钟</p>
          <p><strong>是否有马甲加学员：</strong> {customer.additional_students ? '是' : '否'}</p>
          <p><strong>评论数：</strong> {customer.comments_count ? '是' : '否'}</p>
          <p><strong>是否进行人设聊天：</strong> {customer.persona_chat ? '是' : '否'}</p>
          <p><strong>第一天观后反馈：</strong> {customer.first_day_feedback}</p>
          <p><strong>第二天观后反馈：</strong> {customer.second_day_feedback}</p>
          <p><strong>客户描述：</strong> {customer.description || '无'}</p>
        </section>

        {/* 成交分析 */}
        <section>
          <h2>成交分析</h2>
          <p><strong>7天成交：</strong> {customer.deal_7_days_checked ? '是' : '否'}</p>
          {customer.deal_7_days_checked && <p><strong>7天成交说明：</strong> {customer.deal_7_days_text}</p>}
          <p><strong>14天成交：</strong> {customer.deal_14_days_checked ? '是' : '否'}</p>
          {customer.deal_14_days_checked && <p><strong>14天成交说明：</strong> {customer.deal_14_days_text}</p>}
          <p><strong>21天成交：</strong> {customer.deal_21_days_checked ? '是' : '否'}</p>
          {customer.deal_21_days_checked && <p><strong>21天成交说明：</strong> {customer.deal_21_days_text}</p>}
        </section>

        {/* 系统数据 */}
        <section>
          <h2>系统数据</h2>
          <p><strong>数据来源：</strong> {customer.data_source}</p>
          <p><strong>是否接通：</strong> {customer.is_contacted ? '是' : '否'}</p>
          <p><strong>是否成交：</strong> {customer.is_closed ? '是' : '否'}</p>
          <p><strong>创建人：</strong> {customer.created_by || '未知'}</p>
          <p><strong>最后修改人：</strong> {customer.updated_by || '未知'}</p>
          <p><strong>创建时间：</strong> {new Date(customer.created_at).toLocaleString()}</p>
          <p><strong>修改时间：</strong> {new Date(customer.updated_at).toLocaleString()}</p>
        </section>

        <button className="back-button" onClick={() => navigate('/customers')}>
          返回客户列表
        </button>
      </div>
    </div>
  );
};

export default CustomerDetail;