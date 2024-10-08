import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCustomerById, updateCustomer } from '../api/customerApi';  // API 方法

const EditCustomer = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  // 初始化客户数据状态
  const [customer, setCustomer] = useState({
    name: '',
    phone: '',
    education: '',
    major_category: '',
    status: '',
    address: '',
    city: '',
    is_closed: false,
    is_invited: false,
    is_joined: false,
    data_source: '',
    attended_first_live: false,
    attended_second_live: false,
    first_day_watch_duration: 0,
    second_day_watch_duration: 0,
    description: '',
    intention: '低',  // 默认意向程度
  });

  useEffect(() => {
    loadCustomer();
  }, []);

  // 加载客户信息
  const loadCustomer = async () => {
    try {
      const data = await getCustomerById(id);
      setCustomer(data);
    } catch (error) {
      console.error('加载客户失败:', error);
    }
  };

  // 提交更新
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await updateCustomer(id, customer);
      navigate('/customers');  // 更新成功后跳转回客户列表页面
    } catch (error) {
      console.error('更新客户失败:', error);
    }
  };

  // 处理表单字段的变化
  const handleInputChange = (event) => {
    const { name, value, type, checked } = event.target;
    setCustomer({
      ...customer,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  return (
    <div className="container">
      <h2>编辑客户</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>姓名</label>
          <input
            type="text"
            className="form-control"
            name="name"
            value={customer.name}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label>电话</label>
          <input
            type="text"
            className="form-control"
            name="phone"
            value={customer.phone}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label>学历</label>
          <select
            className="form-control"
            name="education"
            value={customer.education}
            onChange={handleInputChange}
          >
            <option value="大专以下">大专以下</option>
            <option value="大专">大专</option>
            <option value="本科">本科</option>
            <option value="研究生及以上<">研究生及以上</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label>专业类别</label>
          <select
            className="form-control"
            name="major_category"
            value={customer.major_category}
            onChange={handleInputChange}
          >
            <option value="IT">IT</option>
            <option value="非IT">非IT</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label>状态</label>
          <select
            className="form-control"
            name="status"
            value={customer.status}
            onChange={handleInputChange}
          >
            <option value="在职">在职</option>
            <option value="待业">待业</option>
            <option value="未知">未知</option>
          </select>
        </div>

        <div className="form-group">
          <label>就业意向城市</label>
          <input
            type="text"
            className="form-control"
            name="address"
            value={customer.address}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label>当前所在城市</label>
          <input
            type="text"
            className="form-control"
            name="city"
            value={customer.city}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-check">
          <input
            type="checkbox"
            className="form-check-input"
            name="is_closed"
            checked={customer.is_closed}
            onChange={handleInputChange}
          />
          <label className="form-check-label">是否成交</label>
        </div>

        <div className="form-check">
          <input
            type="checkbox"
            className="form-check-input"
            name="is_invited"
            checked={customer.is_invited}
            onChange={handleInputChange}
          />
          <label className="form-check-label">是否邀约</label>
        </div>

        <div className="form-check">
          <input
            type="checkbox"
            className="form-check-input"
            name="is_joined"
            checked={customer.is_joined}
            onChange={handleInputChange}
          />
          <label className="form-check-label">是否入群</label>
        </div>

        <div className="form-group">
          <label>数据来源</label>
          <select
            className="form-control"
            name="data_source"
            value={customer.data_source}
            onChange={handleInputChange}
          >
            <option value="AI数据">AI数据</option>
            <option value="视频号">视频号</option>
            <option value="其他">其他</option>
          </select>
        </div>

        <div className="form-check">
          <input
            type="checkbox"
            className="form-check-input"
            name="attended_first_live"
            checked={customer.attended_first_live}
            onChange={handleInputChange}
          />
          <label className="form-check-label">参加第一天直播</label>
        </div>

        <div className="form-check">
          <input
            type="checkbox"
            className="form-check-input"
            name="attended_second_live"
            checked={customer.attended_second_live}
            onChange={handleInputChange}
          />
          <label className="form-check-label">参加第二天直播</label>
        </div>

        <div className="form-group">
          <label>第一天观看时长</label>
          <input
            type="number"
            className="form-control"
            name="first_day_watch_duration"
            value={customer.first_day_watch_duration}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-group">
          <label>第二天观看时长</label>
          <input
            type="number"
            className="form-control"
            name="second_day_watch_duration"
            value={customer.second_day_watch_duration}
            onChange={handleInputChange}
            required
          />
        </div>

        {/* 意向程度 */}
        <div className="form-group">
          <label>意向程度</label>
          <select
            className="form-control"
            name="intention"
            value={customer.intention}
            onChange={handleInputChange}
          >
            <option value="低">低</option>
            <option value="中">中</option>
            <option value="高">高</option>
          </select>
        </div>

        <div className="form-group">
          <label>客户描述</label>
          <textarea
            className="form-control"
            name="description"
            rows="3"
            value={customer.description}
            onChange={handleInputChange}
          ></textarea>
        </div>

        <button type="submit" className="btn btn-primary">保存</button>
      </form>
    </div>
  );
};

export default EditCustomer;