import React from 'react';
import { Link } from 'react-router-dom';
import { FaCheckCircle, FaTimesCircle, FaExclamationCircle } from 'react-icons/fa';
import './CustomerTable.css'; // 引入局部样式

const CustomerTable = ({ customers, onDelete, currentUser, isViewOnly = false }) => (
  <div className="table-container">
    <table className="customer-table">
      <thead>
        <tr>
          <th>姓名</th>
          <th>电话</th>
          <th>归属人</th>
          <th>创建时间</th>
          <th>数据来源</th>
          <th>期数学员</th>
          <th>是否邀约</th>
          <th>是否加微信</th>
          <th>是否入群</th>
          <th>客户描述</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        {customers.length > 0 ? (
          customers.map((customer) => (
            <tr key={customer.id}>
              <td>
                {customer.name}{' '}
                {customer.created_by !== customer.updated_by && (
                  <FaExclamationCircle className="text-danger" />
                )}
              </td>
              <td>{customer.phone}</td>
              <td>{customer.created_by}</td>
              <td>{new Date(customer.created_at).toLocaleDateString()}</td>
              <td>{customer.data_source}</td>
              <td>{customer.student_batch || 'N/A'}</td>
              
              {/* 是否邀约 */}
              <td>
                {customer.is_invited ? (
                  <FaCheckCircle className="icon-success" />
                ) : (
                  <FaTimesCircle className="icon-danger" />
                )}
              </td>

              {/* 是否加微信 */}
              <td>
                {customer.is_wechat_added ? (
                  <FaCheckCircle className="icon-success" />
                ) : (
                  <FaTimesCircle className="icon-danger" />
                )}
              </td>

              {/* 是否入群 */}
              <td>
                {customer.is_joined ? (
                  <FaCheckCircle className="icon-success" />
                ) : (
                  <FaTimesCircle className="icon-danger" />
                )}
              </td>

              {/* 客户描述 */}
              <td>{customer.description || '暂无描述'}</td>

              {/* 操作列 */}
              <td>
                <div className="btn-group">
                  <Link to={`/customer/${customer.id}`} className="btn btn-info">
                    详情
                  </Link>
                  
                  {/* 显示更新按钮 */}
                  {!isViewOnly &&
                    (currentUser.role === 'admin' || 
                    customer.created_by === currentUser.username) && (
                      <Link to={`/edit-customer/${customer.id}`} className="btn btn-warning">
                        更新
                      </Link>
                    )}

                  {/* 显示删除按钮（组长或管理员） */}
                  {!isViewOnly &&
                    (currentUser.role === 'admin' ||
                      (currentUser.group_id && currentUser.group_id === customer.group_id)) && (
                      <button onClick={() => onDelete(customer.id)} className="btn btn-danger">
                        删除
                      </button>
                    )}
                </div>
              </td>
            </tr>
          ))
        ) : (
          <tr>
            <td colSpan="11" className="no-data">暂无客户数据</td>
          </tr>
        )}
      </tbody>
    </table>
  </div>
);

export default CustomerTable;