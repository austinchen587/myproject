import React from 'react';
import './CommunicationMethodForm.css'; // 引入局部CSS文件

const CommunicationMethodForm = ({ customerData, handleChange }) => {
  const communicationMethods = customerData.communication_methods || [];

  const handleCheckboxChange = (e) => {
    const { value, checked } = e.target;

    let updatedMethods = checked
      ? [...communicationMethods, value]
      : communicationMethods.filter((method) => method !== value);

    handleChange({
      target: { name: 'communication_methods', value: updatedMethods },
    });
  };

  return (
    <div className="communication-method-container">
      <h2 className="section-title">沟通方式</h2>

      <div className="checkbox-group">
        <label className="checkbox-label">
          <input
            type="checkbox"
            name="communication_methods"
            value="电话沟通"
            checked={communicationMethods.includes('电话沟通')}
            onChange={handleCheckboxChange}
          />
          电话沟通
        </label>

        <label className="checkbox-label">
          <input
            type="checkbox"
            name="communication_methods"
            value="微信沟通"
            checked={communicationMethods.includes('微信沟通')}
            onChange={handleCheckboxChange}
          />
          微信沟通
        </label>
      </div>
    </div>
  );
};

export default CommunicationMethodForm;