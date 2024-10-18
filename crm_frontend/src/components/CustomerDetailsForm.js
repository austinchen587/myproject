import React from 'react';
import './CustomerDetailsForm.css'; // 引入CSS文件

const CustomerDetailsForm = ({ customerData, handleChange }) => {
  return (
    <div className="customer-details-container">
      <h2 className="section-title">客户情况</h2>

      {/* 姓名与年龄 */}
      <div className="form-row">
        <div className="form-group">
          <label htmlFor="name">姓名:</label>
          <input
            type="text"
            className="form-control"
            name="name"
            value={customerData.name}
            onChange={handleChange}
            placeholder="请输入客户姓名"
   
          />
        </div>

        <div className="form-group">
          <label htmlFor="age">年龄:</label>
          <input
            type="number"
            className="form-control"
            name="age"
            value={customerData.age}
            onChange={handleChange}
            placeholder="请输入客户年龄"
     
          />
        </div>
      </div>

      {/* 学历与专业 */}
      <div className="form-row">
        <div className="form-group">
          <label htmlFor="education">学历:</label>
          <select
            className="form-control"
            name="education"
            value={customerData.education}
            onChange={handleChange}
          >
            <option value="大专以下">大专以下</option>
            <option value="大专">大专</option>
            <option value="本科">本科</option>
            <option value="研究生及以上">研究生及以上</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="major_category">专业类别:</label>
          <select
            className="form-control"
            name="major_category"
            value={customerData.major_category}
            onChange={handleChange}
          >
            <option value="IT">IT</option>
            <option value="非IT">非IT</option>
            <option value="未知">未知</option>
          </select>
        </div>
      </div>

      {/* 在职状态与所在城市 */}
      <div className="form-row">
        <div className="form-group">
          <label htmlFor="status">状态:</label>
          <select
            className="form-control"
            name="status"
            value={customerData.status}
            onChange={handleChange}
          >
            <option value="在职">在职</option>
            <option value="待业">待业</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="city">所在城市:</label>
          <input
            type="text"
            className="form-control"
            name="city"
            value={customerData.city}
            onChange={handleChange}
            placeholder="请输入所在城市"
            required
          />
        </div>
      </div>
    </div>
  );
};

export default CustomerDetailsForm;