import React from 'react';
import './EditNeedsAndPersonalityForm.css'; // 引入局部样式文件

const EditNeedsAndPersonalityForm = ({ customer, handleMultiSelectChange }) => {
  // 选项列表
  const needsOptions = [
    '是否有知识付费的意识',
    '是否排斥培训',
    '是否被培训机构骗过',
    '是否表示工作难找',
    '找工作有多久',
    '是否想尽快就业',
    '是否想转行',
    '是否了解过云计算',
    '是否认可云计算',
  ];

  const personalityOptions = [
    '犹豫', '理性', '妈宝男', '怕吃苦', '墨迹', '迷茫', '攻击性大', '自我内耗',
  ];

  const cloudComputingPromotionOptions = [
    '云计算小视频+文字简单的概述',
    '云计算有几种服务模式（服务模式对应的场景）',
    '云计算的薪资和发展空间',
    '云计算岗位及对应的工作内容',
    '云计算和数字经济的关联性',
    '行业的介绍（人社局-薪资、缺口、推进方向）',
    '通信院（政策推进和未来发展趋势）',
  ];

  // 确保数据为数组类型，避免出现 undefined 或其他错误
  const customerNeedsAnalysis = customer.customer_needs_analysis || [];
  const customerPersonalityAnalysis = customer.customer_personality_analysis || [];
  const cloudPromotionContent = customer.cloud_computing_promotion_content || [];

  // 检查选中状态
  const isChecked = (name, value) => {
    const fieldArray = customer[name] || [];
    return fieldArray.includes(value);
  };

  // 处理多选框选中/取消状态
  const handleCheckboxChange = (e, fieldName) => {
    const { value, checked } = e.target;
    const updatedArray = checked
      ? [...(customer[fieldName] || []), value]
      : (customer[fieldName] || []).filter((item) => item !== value);

    handleMultiSelectChange(fieldName, updatedArray);
  };

  return (
    <div className="analysis-form-container">
      <h2 className="section-title">客户挖需与性格分析</h2>

      {/* 客户挖需分析 */}
      <div className="form-section">
        <label className="section-subtitle">客户挖需分析:</label>
        <div className="checkbox-group">
          {needsOptions.map((option) => (
            <label key={option} className="checkbox-label">
              <input
                type="checkbox"
                value={option}
                checked={isChecked('customer_needs_analysis', option)}
                onChange={(e) => handleCheckboxChange(e, 'customer_needs_analysis')}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      </div>

      {/* 客户性格分析 */}
      <div className="form-section">
        <label className="section-subtitle">客户性格分析:</label>
        <div className="checkbox-group">
          {personalityOptions.map((option) => (
            <label key={option} className="checkbox-label">
              <input
                type="checkbox"
                value={option}
                checked={isChecked('customer_personality_analysis', option)}
                onChange={(e) => handleCheckboxChange(e, 'customer_personality_analysis')}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      </div>

      {/* 云计算推广内容 */}
      <div className="form-section">
        <label className="section-subtitle">云计算推广内容:</label>
        <div className="checkbox-group">
          {cloudComputingPromotionOptions.map((option) => (
            <label key={option} className="checkbox-label">
              <input
                type="checkbox"
                value={option}
                checked={isChecked('cloud_computing_promotion_content', option)}
                onChange={(e) => handleCheckboxChange(e, 'cloud_computing_promotion_content')}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      </div>
    </div>
  );
};

export default EditNeedsAndPersonalityForm;