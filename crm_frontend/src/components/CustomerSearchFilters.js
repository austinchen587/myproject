import React, { useState } from 'react';
import './CustomerSearchFilters.css'; // 引入局部样式文件

const CustomerSearchFilters = ({
  onOwnerSelect,
  onIntentionSelect,
  onExclamationFilterChange,
  onPhoneSearch,
  selectedOwner,
  selectedIntention,
  filterExclamation,
  ownerOptions,
  onIsContactedFilterChange,
  onIsWechatAddedFilterChange,
  onAttendedFirstLiveFilterChange,
  onAttendedSecondLiveFilterChange,
  onDataSourceSelect,  // 添加数据来源筛选
  isContactedFilter,
  isWechatAddedFilter,
  attendedFirstLiveFilter,
  attendedSecondLiveFilter,
  dataSourceFilter,     // 传递当前数据来源筛选值
}) => {
  const [phoneInput, setPhoneInput] = useState(''); // 用于手机号输入

  // 处理手机号输入变化
  const handlePhoneInputChange = (event) => {
    setPhoneInput(event.target.value);
  };

  // 点击“确定”按钮时，传递手机号搜索的回调
  const handlePhoneSearchClick = () => {
    onPhoneSearch(phoneInput);
  };

  return (
    <div className="customer-filters-container">
      {/* 归属人筛选 */}
      <div>
        <label>归属人：</label>
        <select
          className="form-control"
          value={selectedOwner}
          onChange={(e) => onOwnerSelect(e.target.value)}
        >
          <option value="">全部</option>
          {ownerOptions.map((owner, index) => (
            <option key={index} value={owner}>
              {owner}
            </option>
          ))}
        </select>
      </div>

      {/* 意向程度筛选 */}
      <div>
        <label>意向程度：</label>
        <select
          className="form-control"
          value={selectedIntention}
          onChange={(e) => onIntentionSelect(e.target.value)}
        >
          <option value="">全部</option>
          <option value="高">高</option>
          <option value="中">中</option>
          <option value="低">低</option>
        </select>
      </div>

      {/* 数据来源筛选 */}
      <div>
        <label>数据来源：</label>
        <select
          className="form-control"
          value={dataSourceFilter}
          onChange={(e) => onDataSourceSelect(e.target.value)} // 处理数据来源选择变化
        >
          <option value="">全部</option>
          <option value="AI数据">AI数据</option>
          <option value="视频号">视频号</option>
          <option value="其他">其他</option>
        </select>
      </div>

      {/* 感叹号筛选 */}
      <div className="form-check">
        <input
          className="form-check-input"
          type="checkbox"
          checked={filterExclamation}
          onChange={(e) => onExclamationFilterChange(e.target.checked)}
        />
        <label className="form-check-label">只显示名字带感叹号的客户</label>
      </div>

      {/* 是否接通筛选 */}
      <div className="form-check">
        <input
          className="form-check-input"
          type="checkbox"
          checked={isContactedFilter}
          onChange={(e) => onIsContactedFilterChange(e.target.checked)}
        />
        <label className="form-check-label">是否接通</label>
      </div>

      {/* 是否加微信筛选 */}
      <div className="form-check">
        <input
          className="form-check-input"
          type="checkbox"
          checked={isWechatAddedFilter}
          onChange={(e) => onIsWechatAddedFilterChange(e.target.checked)}
        />
        <label className="form-check-label">是否加微信</label>
      </div>

      {/* 参加第一天直播筛选 */}
      <div className="form-check">
        <input
          className="form-check-input"
          type="checkbox"
          checked={attendedFirstLiveFilter}
          onChange={(e) => onAttendedFirstLiveFilterChange(e.target.checked)}
        />
        <label className="form-check-label">参加第一天直播</label>
      </div>

      {/* 参加第二天直播筛选 */}
      <div className="form-check">
        <input
          className="form-check-input"
          type="checkbox"
          checked={attendedSecondLiveFilter}
          onChange={(e) => onAttendedSecondLiveFilterChange(e.target.checked)}
        />
        <label className="form-check-label">参加第二天直播</label>
      </div>

      {/* 手机号搜索 */}
      <div>
        <label>输入手机号筛选：</label>
        <input
          type="text"
          className="form-control"
          placeholder="输入手机号"
          value={phoneInput}
          onChange={handlePhoneInputChange}
        />
        <button className="btn btn-primary mt-2" onClick={handlePhoneSearchClick}>
          确定
        </button>
      </div>
    </div>
  );
};

export default CustomerSearchFilters;