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

        {/* Text Fields */}
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

        {/* Select Fields */}
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

        <div className="form-group">
          <label htmlFor="major_category">专业类别:</label>
          <select
            className="form-control"
            name="major_category"
            value={customerData.major_category}
            onChange={handleChange}
          >
            <option value="IT">IT</option>
            <option value="非IT">教育</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="status">状态:</label>
          <select
            className="form-control"
            name="status"
            value={customerData.status}
            onChange={handleChange}
          >
            <option value="在职">在职</option>
            <option value="待业">待业</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="intention">意向程度:</label>
          <select
            className="form-control"
            name="intention"
            value={customerData.intention}
            onChange={handleChange}
          >
            <option value="低">低</option>
            <option value="中">中</option>
            <option value="高">高</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="data_source">数据来源:</label>
          <select
            className="form-control"
            name="data_source"
            value={customerData.data_source}
            onChange={handleChange}
          >
            <option value="AI数据">AI数据</option>
            <option value="视频号">视频号</option>
            <option value="未知">其他</option>
          </select>
        </div>

        {/* Checkbox Fields */}
        {[
          { label: '是否成交', name: 'is_closed' },
          { label: '是否接受邀请', name: 'is_invited' },
          { label: '是否入群', name: 'is_joined' },
          { label: '参加第一次直播', name: 'attended_first_live' },
          { label: '参加第二次直播', name: 'attended_second_live' },
        ].map((checkbox) => (
          <div className="form-group" key={checkbox.name}>
            <label htmlFor={checkbox.name}>
              <input
                type="checkbox"
                name={checkbox.name}
                checked={customerData[checkbox.name]}
                onChange={handleChange}
              />
              {checkbox.label}
            </label>
          </div>
        ))}

        {/* Textarea */}
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