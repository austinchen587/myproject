import React from 'react';
import './NeedsAndPersonalityAnalysis.css'; // 引入局部CSS

const NeedsAndPersonalityAnalysis = ({ customerData, handleChange }) => {
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

  const handleCheckboxChange = (e) => {
    const { name, value, checked } = e.target;
    const currentValues = customerData[name] || [];

    const updatedValues = checked
      ? [...currentValues, value]
      : currentValues.filter((item) => item !== value);

    handleChange({ target: { name, value: updatedValues } });
  };

  const isChecked = (name, value) => customerData[name]?.includes(value);

  return (
    <div className="analysis-form-container">
      <h2 className="section-title">客户挖需与分析</h2>

      <div className="form-section">
        <label className="section-subtitle">客户挖需分析</label>
        <div className="checkbox-group">
          {needsOptions.map((option) => (
            <label key={option} className="checkbox-label">
              <input
                type="checkbox"
                name="customer_needs_analysis"
                value={option}
                checked={isChecked('customer_needs_analysis', option)}
                onChange={handleCheckboxChange}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="form-section">
        <label className="section-subtitle">客户性格分析</label>
        <div className="checkbox-group">
          {personalityOptions.map((option) => (
            <label key={option} className="checkbox-label">
              <input
                type="checkbox"
                name="customer_personality_analysis"
                value={option}
                checked={isChecked('customer_personality_analysis', option)}
                onChange={handleCheckboxChange}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="form-section">
        <label className="section-subtitle">云计算推广内容</label>
        <div className="checkbox-group">
          {cloudComputingPromotionOptions.map((option) => (
            <label key={option} className="checkbox-label">
              <input
                type="checkbox"
                name="cloud_computing_promotion_content"
                value={option}
                checked={isChecked('cloud_computing_promotion_content', option)}
                onChange={handleCheckboxChange}
              />
              <span>{option}</span>
            </label>
          ))}
        </div>
      </div>
    </div>
  );
};

export default NeedsAndPersonalityAnalysis;