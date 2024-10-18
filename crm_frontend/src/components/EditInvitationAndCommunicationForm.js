import React from 'react';
import './EditInvitationAndCommunicationForm.css';  // 引入局部样式

const EditInvitationAndCommunicationForm = ({ customer, handleInputChange }) => (
  <div className="invitation-communication-form">
    <div className="form-check custom-check">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="is_invited"
        checked={customer.is_invited}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否邀约</label>
    </div>

    <div className="form-group">
      <label>沟通方式</label>
      <input
        type="text"
        className="form-control custom-input"
        name="communication_methods"
        value={customer.communication_methods}
        onChange={handleInputChange}
        placeholder="输入沟通方式"
      />
    </div>

    <div className="form-check custom-check">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="is_wechat_added"
        checked={customer.is_wechat_added}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否加微信</label>
    </div>

    <div className="form-group">
      <label>客户微信名</label>
      <input
        type="text"
        className="form-control custom-input"
        name="wechat_name"
        value={customer.wechat_name}
        onChange={handleInputChange}
        placeholder="输入微信名"
      />
    </div>

    <div className="form-check custom-check">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="is_joined"
        checked={customer.is_joined}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否入群</label>
    </div>
  </div>
);

export default EditInvitationAndCommunicationForm;