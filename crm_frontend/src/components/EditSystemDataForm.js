import React from 'react';
import './EditSystemDataForm.css';  // 引入局部样式文件

const EditSystemDataForm = ({ customer, handleInputChange }) => (
  <div className="edit-system-data-form-container">
    <h2 className="section-title">系统数据</h2>

    <div className="form-group">
      <label className="form-label">数据来源</label>
      <select
        className="form-control custom-input"
        name="data_source"
        value={customer.data_source || 'AI数据'}
        onChange={handleInputChange}
      >
        <option value="AI数据">AI数据</option>
        <option value="视频号">视频号</option>
        <option value="其他">其他</option>
      </select>
    </div>

    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input"
        name="is_contacted"
        checked={customer.is_contacted || false}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否接通</label>
    </div>

    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input"
        name="is_closed"
        checked={customer.is_closed || false}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否成交</label>
    </div>
  </div>
);

export default EditSystemDataForm;