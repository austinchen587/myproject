import React from 'react';
import './WeChatForm.css';

const WeChatForm = ({ customerData, handleChange }) => {
  return (
    <div className="wechat-form-container">
      <h2 className="section-title">微信信息</h2>

      <div className="form-group">
        <label htmlFor="is_wechat_added" className="checkbox-label">
          <input
            type="checkbox"
            name="is_wechat_added"
            checked={customerData.is_wechat_added}
            onChange={handleChange}
          />
          <span className="checkbox-text">是否加微信</span>
        </label>
      </div>

      {customerData.is_wechat_added && (
        <>
          <div className="form-group">
            <label htmlFor="wechat_name">客户微信名字:</label>
            <input
              type="text"
              className="form-control"
              name="wechat_name"
              value={customerData.wechat_name}
              onChange={handleChange}
              maxLength={50}
              placeholder="请输入微信名"
            />
          </div>

          <div className="form-group">
            <label htmlFor="is_joined" className="checkbox-label">
              <input
                type="checkbox"
                name="is_joined"
                checked={customerData.is_joined}
                onChange={handleChange}
              />
              <span className="checkbox-text">是否加入微信群</span>
            </label>
          </div>
        </>
      )}
    </div>
  );
};

export default WeChatForm;