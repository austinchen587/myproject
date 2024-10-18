import React, { useState } from 'react';
import './CustomerSearchFilters.css'; // 引入局部样式文件

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
      <select
        name="owner"
        value={filters.owner}
        onChange={handleInputChange}
        className="filter-select"
      >
        <option value="">归属人</option>
        {ownerOptions.map((owner, index) => (
          <option key={index} value={owner}>
            {owner}
          </option>
        ))}
      </select>

      <select
        name="studentBatch"
        value={filters.studentBatch}
        onChange={handleInputChange}
        className="filter-select"
      >
        <option value="">期数学员</option>
        {studentBatchOptions.map((batch, index) => (
          <option key={index} value={batch}>
            {batch}
          </option>
        ))}
      </select>

      <select
        name="dataSource"
        value={filters.dataSource}
        onChange={handleInputChange}
        className="filter-select"
      >
        <option value="">数据来源</option>
        <option value="AI数据">AI数据</option>
        <option value="视频号">视频号</option>
        <option value="其他">其他</option>
      </select>

      <div className="checkbox-item">
        <input
          type="checkbox"
          name="filterExclamation"
          checked={filters.filterExclamation}
          onChange={handleCheckboxChange}
          className="filter-checkbox"
        />
        <label>筛选红色感叹号</label>
      </div>

      <input
        type="text"
        className="filter-input"
        placeholder="输入电话号码"
        value={phoneInput}
        onChange={(e) => setPhoneInput(e.target.value)}
      />
      <button className="btn search-btn" onClick={handlePhoneSearch}>
        搜索
      </button>

      {['7天成交', '14天成交', '21天成交'].map((label, idx) => (
        <div key={idx} className="checkbox-item">
          <input
            type="checkbox"
            name={`deal${7 * (idx + 1)}Days`}
            checked={filters[`deal${7 * (idx + 1)}Days`]}
            onChange={handleCheckboxChange}
            className="filter-checkbox"
          />
          <label>{label}</label>
        </div>
      ))}
    </div>
  );
};

export default CustomerSearchFilters;