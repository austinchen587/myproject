import React, { useState } from 'react';
import './CustomerSearchFilters.css';

const CustomerSearchFilters = ({ filters, onFilterChange, ownerOptions, studentBatchOptions }) => {
  const [phoneInput, setPhoneInput] = useState(filters.searchPhone || '');

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
    <div className="search-filters-wrapper">
      <div className="search-filters-row">
        <select name="owner" value={filters.owner} onChange={handleInputChange}>
          <option value="">归属人</option>
          {ownerOptions.map((owner, index) => (
            <option key={index} value={owner}>{owner}</option>
          ))}
        </select>

        <select name="studentBatch" value={filters.studentBatch} onChange={handleInputChange}>
          <option value="">期数学员</option>
          {studentBatchOptions.map((batch, index) => (
            <option key={index} value={batch}>{batch}</option>
          ))}
        </select>

        <select name="dataSource" value={filters.dataSource} onChange={handleInputChange}>
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
          />
          <label>筛选红色感叹号</label>
        </div>

        <div className="phone-search-container">
          <input
            type="text"
            placeholder="输入电话号码"
            value={phoneInput}
            onChange={(e) => setPhoneInput(e.target.value)}
          />
          <button onClick={handlePhoneSearch}>搜索</button>
        </div>

        <div className="checkbox-item">
          <input
            type="checkbox"
            name="deal7Days"
            checked={filters.deal7Days}
            onChange={handleCheckboxChange}
          />
          <label>7天成交</label>
        </div>

        <div className="checkbox-item">
          <input
            type="checkbox"
            name="deal14Days"
            checked={filters.deal14Days}
            onChange={handleCheckboxChange}
          />
          <label>14天成交</label>
        </div>

        <div className="checkbox-item">
          <input
            type="checkbox"
            name="deal21Days"
            checked={filters.deal21Days}
            onChange={handleCheckboxChange}
          />
          <label>21天成交</label>
        </div>
      </div>
    </div>
  );
};

export default CustomerSearchFilters;