import React, { useEffect } from 'react';
import './DealAnalysisForm.css';

const DealAnalysisForm = ({ customerData, handleChange }) => {
  
  // 检查 customerData 的初始状态
  useEffect(() => {
    console.log('DealAnalysisForm - 初始状态:', customerData);
  }, []);

  // 检查输入变化并确保每次更新时都能打印
  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    console.log(`字段变化: ${name} = ${type === 'checkbox' ? checked : value}`);

    handleChange(e); // 保持原逻辑不变
  };

  return (
    <div className="deal-analysis-container">
      <h2 className="section-title">成交分析</h2>

      {/* 7天成交 */}
      <div className="deal-section">
        <label htmlFor="deal_7_days_checked" className="checkbox-label">
          <input
            type="checkbox"
            name="deal_7_days_checked"
            checked={customerData.deal_7_days_checked || false}
            onChange={handleInputChange}
          />
          <span>7天成交</span>
        </label>
        {customerData.deal_7_days_checked && (
          <textarea
            className="form-control"
            name="deal_7_days_text"
            value={customerData.deal_7_days_text || ''}
            onChange={handleInputChange}
            placeholder="请输入至少80字的描述"
            minLength={80}
            required
          />
        )}
      </div>

      {/* 14天成交 */}
      <div className="deal-section">
        <label htmlFor="deal_14_days_checked" className="checkbox-label">
          <input
            type="checkbox"
            name="deal_14_days_checked"
            checked={customerData.deal_14_days_checked || false}
            onChange={handleInputChange}
          />
          <span>14天成交</span>
        </label>
        {customerData.deal_14_days_checked && (
          <textarea
            className="form-control"
            name="deal_14_days_text"
            value={customerData.deal_14_days_text || ''}
            onChange={handleInputChange}
            placeholder="请输入描述内容"
          />
        )}
      </div>

      {/* 21天成交 */}
      <div className="deal-section">
        <label htmlFor="deal_21_days_checked" className="checkbox-label">
          <input
            type="checkbox"
            name="deal_21_days_checked"
            checked={customerData.deal_21_days_checked || false}
            onChange={handleInputChange}
          />
          <span>21天成交</span>
        </label>
        {customerData.deal_21_days_checked && (
          <textarea
            className="form-control"
            name="deal_21_days_text"
            value={customerData.deal_21_days_text || ''}
            onChange={handleInputChange}
            placeholder="请输入描述内容"
          />
        )}
      </div>
    </div>
  );
};

export default DealAnalysisForm;