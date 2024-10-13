import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import apiClient from '../api/apiClient';
import './CustomerAnalysis.css';  // 引入样式文件

const CustomerAnalysis = () => {
  const location = useLocation();
  const { currentUser } = location.state || {};

  const [data, setData] = useState([]);
  const [summary, setSummary] = useState({});
  const [averages, setAverages] = useState({
    total_customers: 0,
    intention_high_ratio: 0,
    intention_mid_ratio: 0,
    intention_low_ratio: 0,
    invited_ratio: 0,
    joined_ratio: 0,
    attended_first_live_ratio: 0,
    attended_second_live_ratio: 0,
    closed_ratio: 0,
  });
  const [totalGroupCustomers, setTotalGroupCustomers] = useState(0); // 全组总客户数
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [reportType, setReportType] = useState('daily');
  const [groupLeader, setGroupLeader] = useState('');  // 选择的组长
  const [groupLeaders, setGroupLeaders] = useState([]);  // 组长列表

  useEffect(() => {
    if (currentUser) {
      const fetchData = async () => {
        try {
          let params = { report_type: reportType };
          if (groupLeader) {
            params.group_id = groupLeader;  // 按组长过滤
          }

          const response = await apiClient.get('/customer-analysis/', { params });
          setData(response.data.data);
          setSummary(response.data.summary);
          setAverages(response.data.averages || averages);  // 获取各组的平均值
          setTotalGroupCustomers(response.data.total_group_customers);  // 获取全组总客户数
          setGroupLeaders(response.data.group_leaders);  // 获取组长列表

          setLoading(false);
        } catch (error) {
          setError('无法获取数据');
          setLoading(false);
        }
      };

      fetchData();
    }
  }, [currentUser, reportType, groupLeader]);

  // 颜色渲染逻辑
  const getColorForText = (value, average, isReversed = false) => {
    const diff = value - average;
    const absDiff = Math.abs(diff);
    const intensity = Math.min(255, Math.floor(absDiff * 50)); // 颜色深度控制，最大255
    const color = diff < 0
      ? (isReversed ? `rgb(0, ${intensity}, 0)` : `rgb(${intensity}, 0, 0)`)
      : (isReversed ? `rgb(${intensity}, 0, 0)` : `rgb(0, ${intensity}, 0)`);
    return { color: color };
  };

  if (loading) {
    return <p className="loading-indicator">加载中...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  return (
    <div className="customer-analysis-container">
      <h2>客户数据分析</h2>

      <label>选择报表类型：</label>
      <select value={reportType} onChange={e => setReportType(e.target.value)}>
        <option value="daily">日报</option>
        <option value="weekly">周报</option>
        <option value="monthly">月报</option>
      </select>

      {/* 管理员可以选择组长 */}
      {currentUser?.role === 'admin' && (
        <>
          <label>选择组长：</label>
          <select value={groupLeader} onChange={e => setGroupLeader(e.target.value)}>
            <option value="">全公司</option>
            {groupLeaders.map((leader) => (
              <option key={leader.id} value={leader.id}>
                {leader.username}
              </option>
            ))}
          </select>
        </>
      )}

      <div className="table-container">
        <table border="1">
          <thead>
            <tr>
              <th>用户</th>
              <th>总客户数</th>  {/* 直接显示总客户数 */}
              <th>高意向比例 (%)</th>
              <th>中意向比例 (%)</th>
              <th>低意向比例 (%)</th>
              <th>邀约比例 (%)</th>
              <th>入群比例 (%)</th>
              <th>第一天直播比例 (%)</th>
              <th>第二天直播比例 (%)</th>
              <th>成交比例 (%)</th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                <td>{row['created_by__username']}</td>  {/* 用户名 */}
                <td>{row.total_customers}</td>  {/* 直接显示总客户数 */}
                <td style={getColorForText(row.intention_high_ratio, averages.intention_high_ratio)}>{row.intention_high_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.intention_mid_ratio, averages.intention_mid_ratio, true)}>{row.intention_mid_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.intention_low_ratio, averages.intention_low_ratio, true)}>{row.intention_low_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.invited_ratio, averages.invited_ratio)}>{row.invited_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.joined_ratio, averages.joined_ratio)}>{row.joined_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.attended_first_live_ratio, averages.attended_first_live_ratio)}>{row.attended_first_live_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.attended_second_live_ratio, averages.attended_second_live_ratio)}>{row.attended_second_live_ratio.toFixed(2)}%</td>
                <td style={getColorForText(row.closed_ratio, averages.closed_ratio)}>{row.closed_ratio.toFixed(2)}%</td>
              </tr>
            ))}

            {/* 添加平均值行 */}
            <tr>
              <td><strong>全组平均值</strong></td>
              <td>{summary.total_customers}</td>  {/* 全组总客户数 */}
              <td>{totalGroupCustomers > 0 ? averages.intention_high_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.intention_mid_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.intention_low_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.invited_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.joined_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.attended_first_live_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.attended_second_live_ratio.toFixed(2) : '0'}%</td>
              <td>{totalGroupCustomers > 0 ? averages.closed_ratio.toFixed(2) : '0'}%</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="summary">
        <h3>汇总信息：</h3>
        <p>总客户数: {summary.total_customers}</p>  {/* 全组总客户数 */}
        <p>成交客户数: {summary.total_closed}</p>
      </div>
    </div>
  );
};

export default CustomerAnalysis;