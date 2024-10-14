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
    is_contacted: false, // 是否接通
    is_wechat_added: false, // 是否加微信
    description: '',
    intention: '低'
  });

  const navigate = useNavigate();

  // 处理表单字段的变化，包括复选框的布尔值
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setCustomerData((prevData) => ({
      ...prevData,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  // 提交表单的处理函数
  const handleSubmit = async (e) => {
    e.preventDefault();

    // 打印检查是否接通的状态是否为 true
    console.log("是否接通:", customerData.is_contacted);

    try {
      await addCustomer(customerData); // 提交客户数据
      alert('客户添加成功！');
      navigate('/customers'); // 提交成功后跳转到客户列表
    } catch (error) {
      alert('添加客户失败');
    }
  };

  return (
    <div className="add-customer-container">
      <h1 className="form-title">添加客户</h1>
      <form onSubmit={handleSubmit} className="add-customer-form">

        {/* 数据来源 */}
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

        {/* 是否接通 */}
        <div className="form-group">
          <label htmlFor="is_contacted">
            <input
              type="checkbox"
              name="is_contacted"
              checked={customerData.is_contacted}
              onChange={handleChange} // 确保复选框的状态在变化时被正确更新
            />
            是否接通
          </label>
        </div>

        {/* 意向程度 */}
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

        {/* 姓名 */}
        <div className="form-group">
          <label htmlFor="name">姓名:</label>
          <input
            type="text"
            className="form-control"
            name="name"
            value={customerData.name}
            onChange={handleChange}
            required
          />
        </div>

        {/* 电话 */}
        <div className="form-group">
          <label htmlFor="phone">电话:</label>
          <input
            type="text"
            className="form-control"
            name="phone"
            value={customerData.phone}
            onChange={handleChange}
            required
          />
        </div>

        {/* 学历 */}
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

        {/* 专业类别 */}
        <div className="form-group">
          <label htmlFor="major_category">专业类别:</label>
          <select
            className="form-control"
            name="major_category"
            value={customerData.major_category}
            onChange={handleChange}
          >
            <option value="IT">IT</option>
            <option value="非IT">非IT</option>
            <option value="未知">未知</option>
          </select>
        </div>

        {/* 状态 */}
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

        {/* 当前所在城市 */}
        <div className="form-group">
          <label htmlFor="city">当前所在城市:</label>
          <input
            type="text"
            className="form-control"
            name="city"
            value={customerData.city}
            onChange={handleChange}
          />
        </div>

        {/* 就业意向城市 */}
        <div className="form-group">
          <label htmlFor="address">就业意向城市:</label>
          <input
            type="text"
            className="form-control"
            name="address"
            value={customerData.address}
            onChange={handleChange}
          />
        </div>

        {/* 是否加微信 */}
        <div className="form-group">
          <label htmlFor="is_wechat_added">
            <input
              type="checkbox"
              name="is_wechat_added"
              checked={customerData.is_wechat_added}
              onChange={handleChange}
            />
            是否加微信
          </label>
        </div>

        {/* 是否接受邀请 */}
        <div className="form-group">
          <label htmlFor="is_invited">
            <input
              type="checkbox"
              name="is_invited"
              checked={customerData.is_invited}
              onChange={handleChange}
            />
            是否接受邀请
          </label>
        </div>

        {/* 是否入群 */}
        <div className="form-group">
          <label htmlFor="is_joined">
            <input
              type="checkbox"
              name="is_joined"
              checked={customerData.is_joined}
              onChange={handleChange}
            />
            是否入群
          </label>
        </div>

        {/* 参加第一次直播 */}
        <div className="form-group">
          <label htmlFor="attended_first_live">
            <input
              type="checkbox"
              name="attended_first_live"
              checked={customerData.attended_first_live}
              onChange={handleChange}
            />
            参加第一次直播
          </label>
        </div>

        {/* 第一日观看时长 */}
        <div className="form-group">
          <label htmlFor="first_day_watch_duration">第一天观看时长:</label>
          <input
            type="number"
            className="form-control"
            name="first_day_watch_duration"
            value={customerData.first_day_watch_duration}
            onChange={handleChange}
          />
        </div>

        {/* 参加第二次直播 */}
        <div className="form-group">
          <label htmlFor="attended_second_live">
            <input
              type="checkbox"
              name="attended_second_live"
              checked={customerData.attended_second_live}
              onChange={handleChange}
            />
            参加第二次直播
          </label>
        </div>

        {/* 第二日观看时长 */}
        <div className="form-group">
          <label htmlFor="second_day_watch_duration">第二天观看时长:</label>
          <input
            type="number"
            className="form-control"
            name="second_day_watch_duration"
            value={customerData.second_day_watch_duration}
            onChange={handleChange}
          />
        </div>

        {/* 是否成交 */}
        <div className="form-group">
          <label htmlFor="is_closed">
            <input
              type="checkbox"
              name="is_closed"
              checked={customerData.is_closed}
              onChange={handleChange}
            />
            是否成交
          </label>
        </div>

        {/* 客户描述 */}
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