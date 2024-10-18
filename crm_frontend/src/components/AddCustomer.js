import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import BasicInfoForm from './BasicInfoForm';
import InvitationForm from './InvitationForm';
import CommunicationMethodForm from './CommunicationMethodForm';
import WeChatForm from './WeChatForm';
import CustomerDetailsForm from './CustomerDetailsForm';
import NeedsAndPersonalityAnalysis from './NeedsAndPersonalityAnalysis';
import AttendanceForm from './AttendanceForm';
import DealAnalysisForm from './DealAnalysisForm';
import './AddCustomer.css'; // 引入局部CSS

const AddCustomer = () => {
  const [customerData, setCustomerData] = useState({ is_invited: false });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setCustomerData((prevData) => ({
      ...prevData,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('/api/customers/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(customerData),
      });

      if (!response.ok) {
        throw new Error('提交失败，请重试');
      }

      alert('客户添加成功');
      navigate('/customers');
    } catch (err) {
      console.error('提交错误:', err);
      setError('提交失败，请检查数据并重试');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="add-customer-container">
      <h1 className="add-customer-title">添加客户</h1>
      <form onSubmit={handleSubmit} className="add-customer-form">

        <BasicInfoForm customerData={customerData} handleChange={handleChange} />
        <InvitationForm customerData={customerData} handleChange={handleChange} />

        {customerData.is_invited && (
          <>
            <CommunicationMethodForm customerData={customerData} handleChange={handleChange} />
            <WeChatForm customerData={customerData} handleChange={handleChange} />
            <CustomerDetailsForm customerData={customerData} handleChange={handleChange} />
            <NeedsAndPersonalityAnalysis customerData={customerData} handleChange={handleChange} />
            <AttendanceForm customerData={customerData} handleChange={handleChange} />
            <DealAnalysisForm customerData={customerData} handleChange={handleChange} />
          </>
        )}

        <div className="form-actions">
          <button type="submit" className="submit-button" disabled={loading}>
            {loading ? '提交中...' : '提交'}
          </button>
        </div>

        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  );
};

export default AddCustomer;