import React from 'react';
import './BasicInfoForm.css'; // 引入局部 CSS 文件

const BasicInfoForm = ({ customerData, handleChange }) => {
  return (
    <div className="basic-info-container">
      <h2 className="section-title">基本信息</h2>

      {/* 电话号码 */}
      <div className="form-group">
        <label htmlFor="phone" className="form-label">电话 (11位):</label>
        <input
          type="text"
          className="form-input"
          name="phone"
          value={customerData.phone || ''}
          onChange={handleChange}
          required
          pattern="\d{11}"
          title="请输入11位的电话号码"
          placeholder="请输入11位电话号码"
        />
      </div>

      {/* 期期学员 */}
      <div className="form-group">
        <label htmlFor="student_batch" className="form-label">期期学员:</label>
        <input
          type="number"
          className="form-input"
          name="student_batch"
          value={customerData.student_batch || ''}
          onChange={handleChange}
          required
          placeholder="请输入期数"
        />
      </div>

      {/* 数据来源 */}
      <div className="form-group">
        <label htmlFor="data_source" className="form-label">数据来源:</label>
        <select
          className="form-input"
          name="data_source"
          value={customerData.data_source || ''}
          onChange={handleChange}
          required
        >
          <option value="" disabled>请选择数据来源</option>
          <option value="AI数据">AI数据</option>
          <option value="视频号">视频号</option>
          <option value="其他">其他</option>
        </select>
      </div>
    </div>
  );
};

export default BasicInfoForm;