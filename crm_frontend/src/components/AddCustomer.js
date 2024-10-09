import React, { useState } from 'react';
import { addCustomer } from '../api/customerApi';
import { useNavigate } from 'react-router-dom';
import './AddCustomer.css';

const AddCustomer = () => {
  const [customerData, setCustomerData] = useState({
    name: '',
    phone: '',
    education: '本科',
    major_category: 'IT',
    status: '在职',
    address: '',
    city: '',
    is_closed: false,
    is_invited: false,
    is_joined: false,
    data_source: 'AI数据',
    attended_first_live: false,
    attended_second_live: false,
    first_day_watch_duration: 0,
    second_day_watch_duration: 0,
    description: '',
    intention: '低'
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setCustomerData((prevData) => ({
      ...prevData,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addCustomer(customerData);
      alert('客户添加成功！');
      navigate('/customers');
    } catch (error) {
      alert('添加客户失败');
    }
  };

  return (
    <div className="add-customer-container">
      <h1 className="form-title">添加客户</h1>
      <form onSubmit={handleSubmit} className="add-customer-form">
        {[
          { label: '姓名', name: 'name', type: 'text', required: true },
          { label: '电话', name: 'phone', type: 'text', required: true },
          { label: '就业意向城市', name: 'address', type: 'text' },
          { label: '当前所在城市', name: 'city', type: 'text' },
          { label: '第一天观看时长', name: 'first_day_watch_duration', type: 'number' },
          { label: '第二天观看时长', name: 'second_day_watch_duration', type: 'number' },
        ].map((input) => (
          <div className="form-group" key={input.name}>
            <label htmlFor={input.name}>{input.label}:</label>
            <input
              type={input.type}
              className="form-control"
              name={input.name}
              value={customerData[input.name]}
              onChange={handleChange}
              required={input.required}
            />
          </div>
        ))}

        <div className="form-group">
          <label htmlFor="education">学历:</label>
          <select
            className="form-control"
            name="education"
            value={customerData.education}
            onChange={handleChange}
          >
            <option value="大专以下">大专以下</option>
            <option value="大专">大专</option>
            <option value="本科">本科</option>
            <option value="研究生及以上">研究生及以上</option>
            <option value="未知">未知</option>
          </select>
        </div>

        {/* Repeat other select and checkbox fields similarly */}
        
        <div className="form-group">
          <label htmlFor="description">客户描述:</label>
          <textarea
            className="form-control"
            name="description"
            value={customerData.description}
            onChange={handleChange}
            rows="3"
          />
        </div>

        <button type="submit" className="btn btn-primary submit-btn">
          提交
        </button>
      </form>
    </div>
  );
};

export default AddCustomer;