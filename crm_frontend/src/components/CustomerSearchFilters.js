import React, { useState, useEffect } from 'react';
import './CustomerSearchFilters.css';

const CustomerSearchFilters = ({
  filters,
  onFilterChange,
  ownerOptions = [],
  studentBatchOptions = [],
}) => {
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

  // 保证在ownerOptions或studentBatchOptions为空时显示提示
  const renderOptions = (options) =>
    options.length > 0 ? (
      options.map((option, index) => (
        <option key={index} value={option}>
          {option}
        </option>
      ))
    ) : (
      <option value="" disabled>
        暂无数据
      </option>
    );

  return (
    <div className="search-filters-wrapper">
      <div className="search-filters-container">
        <select
          name="owner"
          value={filters.owner}
          onChange={handleInputChange}
          className="filter-select"
        >
          <option value="">归属人</option>
          {renderOptions(ownerOptions)}
        </select>

        <select
          name="studentBatch"
          value={filters.studentBatch}
          onChange={handleInputChange}
          className="filter-select"
        >
          <option value="">期数学员</option>
          {renderOptions(studentBatchOptions)}
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
          />
          <label>筛选红色感叹号</label>
        </div>

        <div className="phone-search-container">
          <input
            type="text"
            placeholder="输入电话号码"
            value={phoneInput}
            onChange={(e) => setPhoneInput(e.target.value)}
            className="phone-input"
          />
          <button onClick={handlePhoneSearch} className="search-button">
            搜索
          </button>
        </div>

        <div className="checkbox-group">
          {['7天成交', '14天成交', '21天成交'].map((label, index) => (
            <div className="checkbox-item" key={index}>
              <input
                type="checkbox"
                name={`deal${7 * (index + 1)}Days`}
                checked={filters[`deal${7 * (index + 1)}Days`]}
                onChange={handleCheckboxChange}
              />
              <label>{label}</label>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CustomerSearchFilters;