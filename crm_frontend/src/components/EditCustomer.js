import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import EditBasicInfoForm from './EditBasicInfoForm';
import EditInvitationAndCommunicationForm from './EditInvitationAndCommunicationForm';
import EditNeedsAndPersonalityForm from './EditNeedsAndPersonalityForm';
import EditAttendanceForm from './EditAttendanceForm';
import EditDealAnalysisForm from './EditDealAnalysisForm';
import EditSystemDataForm from './EditSystemDataForm';

const EditCustomer = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [customer, setCustomer] = useState({
    name: '',
    phone: '',
    education: '',
    major_category: '',
    status: '',
    city: '',
    is_invited: false,
    communication_methods: '',
    is_wechat_added: false,
    wechat_name: '',
    is_joined: false,
    customer_needs_analysis: [],
    customer_personality_analysis: [],
    cloud_computing_promotion_content: [],
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadCustomer = async () => {
      try {
        setLoading(true);
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('Access token 不存在，请重新登录');
        }

        const response = await fetch(`/api/customers/${id}/`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!response.ok) {
          throw new Error(`加载客户数据失败: ${response.statusText}`);
        }

        const data = await response.json();
        setCustomer({
          ...data,
          customer_needs_analysis: data.customer_needs_analysis || [],
          customer_personality_analysis: data.customer_personality_analysis || [],
          cloud_computing_promotion_content: data.cloud_computing_promotion_content || [],
          communication_methods: data.communication_methods || '',
          wechat_name: data.wechat_name || '',
        });
      } catch (err) {
        console.error('加载客户数据失败:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadCustomer();
  }, [id]);

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setCustomer((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleMultiSelectChange = (fieldName, updatedArray) => {
    setCustomer((prev) => ({
      ...prev,
      [fieldName]: updatedArray,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch(`/api/customers/${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(customer),
      });

      if (!response.ok) {
        throw new Error(`更新失败: ${response.statusText}`);
      }

      navigate('/customers');
    } catch (err) {
      console.error('更新失败:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="edit-customer-container">
      {loading && <p>加载中...</p>}
      {error && <p className="error-message">{error}</p>}

      <form onSubmit={handleSubmit}>
        <EditBasicInfoForm customer={customer} handleInputChange={handleInputChange} />
        <EditInvitationAndCommunicationForm customer={customer} handleInputChange={handleInputChange} />
        <EditNeedsAndPersonalityForm customer={customer} handleMultiSelectChange={handleMultiSelectChange} />
        <EditAttendanceForm customer={customer} handleInputChange={handleInputChange} />
        <EditDealAnalysisForm customer={customer} handleInputChange={handleInputChange} />
        <EditSystemDataForm customer={customer} handleInputChange={handleInputChange} />

        <div className="form-group submit-btn-container">
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? '提交中...' : '提交'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditCustomer;