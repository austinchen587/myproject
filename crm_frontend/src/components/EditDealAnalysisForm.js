import React from 'react';
import './EditDealAnalysisForm.css';  // 引入局部样式文件

const EditDealAnalysisForm = ({ customer, handleInputChange }) => (
  <div className="edit-deal-analysis-form-container">
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="deal_7_days_checked"
        checked={customer.deal_7_days_checked}
        onChange={handleInputChange}
      />
      <label className="form-check-label">7天成交</label>
    </div>
    {customer.deal_7_days_checked && (
      <textarea
        className="form-control custom-textarea"
        name="deal_7_days_text"
        value={customer.deal_7_days_text}
        onChange={handleInputChange}
        placeholder="请输入7天成交说明"
        required
      />
    )}

    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="deal_14_days_checked"
        checked={customer.deal_14_days_checked}
        onChange={handleInputChange}
      />
      <label className="form-check-label">14天成交</label>
    </div>
    {customer.deal_14_days_checked && (
      <textarea
        className="form-control custom-textarea"
        name="deal_14_days_text"
        value={customer.deal_14_days_text}
        onChange={handleInputChange}
        placeholder="请输入14天成交说明"
      />
    )}

    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="deal_21_days_checked"
        checked={customer.deal_21_days_checked}
        onChange={handleInputChange}
      />
      <label className="form-check-label">21天成交</label>
    </div>
    {customer.deal_21_days_checked && (
      <textarea
        className="form-control custom-textarea"
        name="deal_21_days_text"
        value={customer.deal_21_days_text}
        onChange={handleInputChange}
        placeholder="请输入21天成交说明"
      />
    )}
  </div>
);

export default EditDealAnalysisForm;