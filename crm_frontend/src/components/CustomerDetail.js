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

  return (
    <div className="customer-detail-container">
      <h2 className="customer-detail-title">客户详情</h2>
      <div className="customer-detail-card">
        <table className="table">
          <tbody>
            {Object.entries({
              "姓名": customer.name,
              "电话": customer.phone,
              "学历": customer.education,
              "专业类别": customer.major_category,
              "状态": customer.status,
              "就业意向城市": customer.address,
              "当前所在城市": customer.city,
              "意向程度": customer.intention,
              "数据来源": customer.data_source,
              "是否邀约": customer.is_invited ? '是' : '否',
              "是否入群": customer.is_joined ? '是' : '否',
              "参加第一天直播": customer.attended_first_live ? '是' : '否',
              "参加第二天直播": customer.attended_second_live ? '是' : '否',
              "第一天观看时长": `${customer.first_day_watch_duration} 分钟`,
              "第二天观看时长": `${customer.second_day_watch_duration} 分钟`,
              "是否成交": customer.is_closed ? '是' : '否',
              "创建人": customer.created_by || '未知',
              "最后修改人": customer.updated_by || '未知',
              "创建时间": new Date(customer.created_at).toLocaleString(),
              "修改时间": new Date(customer.updated_at).toLocaleString(),
              "描述": customer.description || '无描述'
            }).map(([key, value]) => (
              <tr key={key}>
                <th>{key}</th>
                <td>{value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CustomerDetail;