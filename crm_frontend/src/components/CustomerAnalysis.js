import React, { useEffect, useState } from 'react';
import apiClient from '../api/apiClient';
import './CustomerAnalysis.css';  // 引入样式文件

const CustomerAnalysis = () => {
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
  const [reportType, setReportType] = useState('weekly'); // 默认设为周报
  const [startDate, setStartDate] = useState(''); // 自定义开始日期
  const [endDate, setEndDate] = useState(''); // 自定义结束日期
  const [groupLeader, setGroupLeader] = useState(''); // 选择的组长
  const [groupLeaders, setGroupLeaders] = useState([]); // 组长列表

  useEffect(() => {
    const fetchData = async () => {
      try {
        let params = { report_type: reportType };

        // 如果选择了自定义日期，添加到请求参数
        if (startDate) {
          params.start_date = startDate;
        }
        if (endDate) {
          params.end_date = endDate;
        }
        if (groupLeader) {
          params.group_id = groupLeader; // 按组长过滤
        }

        const response = await apiClient.get('/customer-analysis/', { params });
        setData(response.data.data);
        setSummary(response.data.summary);
        setAverages(response.data.averages || averages); // 获取各组的平均值
        setTotalGroupCustomers(response.data.total_group_customers); // 获取全组总客户数
        setGroupLeaders(response.data.group_leaders); // 获取组长列表

        setLoading(false);
      } catch (error) {
        setError('无法获取数据');
        setLoading(false);
      }
    };

    fetchData();
  }, [reportType, startDate, endDate, groupLeader]);

  const handleReportTypeChange = (event) => {
    setReportType(event.target.value);
  };

  const handleStartDateChange = (event) => {
    setStartDate(event.target.value);
  };

  const handleEndDateChange = (event) => {
    setEndDate(event.target.value);
  };

  const handleGroupLeaderChange = (event) => {
    setGroupLeader(event.target.value);
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

      {/* 报表类型选择 */}
      <label>选择报表类型：</label>
      <select value={reportType} onChange={handleReportTypeChange}>
        <option value="daily">日报</option>
        <option value="weekly">周报</option>
        <option value="monthly">月报</option>
      </select>

      {/* 组长筛选 */}
      <label>选择组长：</label>
      <select value={groupLeader} onChange={handleGroupLeaderChange}>
        <option value="">全公司</option>
        {groupLeaders.map((leader) => (
          <option key={leader.id} value={leader.id}>
            {leader.username}
          </option>
        ))}
      </select>

      {/* 自定义日期选择 */}
      {reportType === 'weekly' && (
        <>
          <div>
            <label>开始日期：</label>
            <input type="date" value={startDate} onChange={handleStartDateChange} />
          </div>
          <div>
            <label>结束日期：</label>
            <input type="date" value={endDate} onChange={handleEndDateChange} />
          </div>
        </>
      )}

      <table className="table">
        <thead>
          <tr>
            <th>用户</th>
            <th>总客户数 (%)</th>
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
              <td>{row['created_by__username']}</td>
              <td>{row.total_customers}</td>
              <td>{row.intention_high_ratio.toFixed(2)}%</td>
              <td>{row.intention_mid_ratio.toFixed(2)}%</td>
              <td>{row.intention_low_ratio.toFixed(2)}%</td>
              <td>{row.invited_ratio.toFixed(2)}%</td>
              <td>{row.joined_ratio.toFixed(2)}%</td>
              <td>{row.attended_first_live_ratio.toFixed(2)}%</td>
              <td>{row.attended_second_live_ratio.toFixed(2)}%</td>
              <td>{row.closed_ratio.toFixed(2)}%</td>
            </tr>
          ))}

          {/* 添加平均值行 */}
          <tr>
            <td><strong>全组平均值</strong></td>
            <td>{summary.total_customers}</td>
            <td>{averages.intention_high_ratio.toFixed(2)}%</td>
            <td>{averages.intention_mid_ratio.toFixed(2)}%</td>
            <td>{averages.intention_low_ratio.toFixed(2)}%</td>
            <td>{averages.invited_ratio.toFixed(2)}%</td>
            <td>{averages.joined_ratio.toFixed(2)}%</td>
            <td>{averages.attended_first_live_ratio.toFixed(2)}%</td>
            <td>{averages.attended_second_live_ratio.toFixed(2)}%</td>
            <td>{averages.closed_ratio.toFixed(2)}%</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default CustomerAnalysis;