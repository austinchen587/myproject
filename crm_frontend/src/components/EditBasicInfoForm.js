import React from 'react';
import './EditBasicInfoForm.css'; // 引入局部样式文件

const EditBasicInfoForm = ({ customer, handleInputChange }) => (
  <div className="edit-basic-info-container">
    {/* 姓名 */}
    <div className="form-group">
      <label>姓名</label>
      <input
        type="text"
        className="form-control custom-input"
        name="name"
        value={customer.name}
        onChange={handleInputChange}
        placeholder="请输入姓名"
      />
    </div>

    {/* 电话 */}
    <div className="form-group">
      <label>电话</label>
      <input
        type="text"
        className="form-control custom-input"
        name="phone"
        value={customer.phone}
        onChange={handleInputChange}
        placeholder="请输入电话号码"
      />
    </div>

    {/* 学历 */}
    <div className="form-group">
      <label>学历</label>
      <select
        className="form-control custom-select"
        name="education"
        value={customer.education}
        onChange={handleInputChange}
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
      <label>专业类别</label>
      <select
        className="form-control custom-select"
        name="major_category"
        value={customer.major_category}
        onChange={handleInputChange}
      >
        <option value="IT">IT</option>
        <option value="非IT">非IT</option>
        <option value="未知">未知</option>
      </select>
    </div>

    {/* 状态 */}
    <div className="form-group">
      <label>状态</label>
      <select
        className="form-control custom-select"
        name="status"
        value={customer.status}
        onChange={handleInputChange}
      >
        <option value="在职">在职</option>
        <option value="待业">待业</option>
        <option value="未知">未知</option>
      </select>
    </div>

    {/* 当前所在城市 */}
    <div className="form-group">
      <label>当前所在城市</label>
      <input
        type="text"
        className="form-control custom-input"
        name="city"
        value={customer.city}
        onChange={handleInputChange}
        placeholder="请输入城市"
      />
    </div>

    {/* 期数学员 */}
    <div className="form-group">
      <label>期数学员</label>
      <input
        type="number"
        className="form-control custom-input"
        name="student_batch"
        value={customer.student_batch || ''}
        onChange={handleInputChange}
        placeholder="请输入期数"
      />
    </div>
  </div>
);

export default EditBasicInfoForm;