import React, { useState } from 'react';
import './CustomerSearchFilters.css'; // 局部样式文件

const CustomerSearchFilters = ({ filters, onFilterChange, ownerOptions, studentBatchOptions }) => {
  const [phoneInput, setPhoneInput] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    onFilterChange({ [name]: value });
  };

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    onFilterChange({ [name]: checked });
  };

  const handlePhoneSearch = () => {
    onFilterChange({ searchPhone: phoneInput });
  };

  return (
    <div className="search-filters-container">
      <div className="filter-group">
        <label>归属人</label>
        <select name="owner" value={filters.owner} onChange={handleInputChange} className="filter-select">
          <option value="">选择归属人</option>
          {ownerOptions.map((owner, index) => (
            <option key={index} value={owner}>
              {owner}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-group">
        <label>期数学员</label>
        <select name="studentBatch" value={filters.studentBatch} onChange={handleInputChange} className="filter-select">
          <option value="">选择期数</option>
          {studentBatchOptions.map((batch, index) => (
            <option key={index} value={batch}>
              {batch}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-group">
        <label>数据来源</label>
        <select name="dataSource" value={filters.dataSource} onChange={handleInputChange} className="filter-select">
          <option value="">选择数据来源</option>
          <option value="AI数据">AI数据</option>
          <option value="视频号">视频号</option>
          <option value="其他">其他</option>
        </select>
      </div>

      <div className="filter-group">
        <label>电话号码</label>
        <input type="text" className="filter-input" placeholder="输入电话号码" value={phoneInput} onChange={(e) => setPhoneInput(e.target.value)} />
        <button className="btn search-btn" onClick={handlePhoneSearch}>搜索</button>
      </div>

      <div className="filter-checkbox-group">
        {['7天成交', '14天成交', '21天成交'].map((label, idx) => (
          <div key={idx} className="checkbox-item">
            <input type="checkbox" name={`deal${7 * (idx + 1)}Days`} checked={filters[`deal${7 * (idx + 1)}Days`]} onChange={handleCheckboxChange} />
            <label>{label}</label>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CustomerSearchFilters;