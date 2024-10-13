import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getCustomerById } from '../api/customerApi';
import './CustomerDetail.css';

const CustomerDetail = () => {
  const { id } = useParams();
  const [customer, setCustomer] = useState(null);

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

  // 判断是否由非创建人进行修改
  const isUpdatedByDifferentUser = customer.created_by !== customer.updated_by;

  return (
    <div className="customer-detail-container">
      <h2 className="customer-detail-title">客户详情</h2>
      <div className="customer-detail-card">
        <table className="table table-bordered">
          <tbody>
            <tr>
              <th>姓名</th>
              <td>{customer.name}</td>
            </tr>
            <tr>
              <th>电话</th>
              <td>{customer.phone}</td>
            </tr>
            <tr>
              <th>学历</th>
              <td>{customer.education}</td>
            </tr>
            <tr>
              <th>专业类别</th>
              <td>{customer.major_category}</td>
            </tr>
            <tr>
              <th>状态</th>
              <td>{customer.status}</td>
            </tr>
            <tr>
              <th>就业意向城市</th>
              <td>{customer.address}</td>
            </tr>
            <tr>
              <th>当前所在城市</th>
              <td>{customer.city}</td>
            </tr>
            <tr>
              <th>意向程度</th>
              <td>{customer.intention}</td>
            </tr>
            <tr>
              <th>数据来源</th>
              <td>{customer.data_source}</td>
            </tr>
            <tr>
              <th>是否邀约</th>
              <td>{customer.is_invited ? '是' : '否'}</td>
            </tr>
            <tr>
              <th>是否入群</th>
              <td>{customer.is_joined ? '是' : '否'}</td>
            </tr>
            <tr>
              <th>参加第一天直播</th>
              <td>{customer.attended_first_live ? '是' : '否'}</td>
            </tr>
            <tr>
              <th>参加第二天直播</th>
              <td>{customer.attended_second_live ? '是' : '否'}</td>
            </tr>
            <tr>
              <th>第一天观看时长</th>
              <td>{customer.first_day_watch_duration} 分钟</td>
            </tr>
            <tr>
              <th>第二天观看时长</th>
              <td>{customer.second_day_watch_duration} 分钟</td>
            </tr>
            <tr>
              <th>是否成交</th>
              <td>{customer.is_closed ? '是' : '否'}</td>
            </tr>
            <tr>
              <th>创建人</th>
              <td>{customer.created_by || '未知'}</td>
            </tr>
            <tr>
              <th>最后修改人</th>
              <td>{customer.updated_by || '未知'}</td>
            </tr>
            <tr>
              <th>创建时间</th>
              <td>{new Date(customer.created_at).toLocaleString()}</td>
            </tr>
            <tr>
              <th>修改时间</th>
              <td>{new Date(customer.updated_at).toLocaleString()}</td>
            </tr>
            <tr>
              <th>描述</th>
              <td style={{ color: isUpdatedByDifferentUser ? 'red' : 'black' }}>
                {customer.description || '无描述'}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CustomerDetail;