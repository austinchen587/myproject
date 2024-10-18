// InvitationForm.js
import React from 'react';

const InvitationForm = ({ customerData, handleChange }) => {
  return (
    <div className="form-group">
      <label htmlFor="is_invited">
        <input
          type="checkbox"
          name="is_invited"
          checked={customerData.is_invited}
          onChange={handleChange}
        />
        是否接受邀约
      </label>
    </div>
  );
};

export default InvitationForm;