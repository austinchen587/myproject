import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getCustomers } from '../api/customerApi';  // 从API获取客户数据
import CustomerSearchFilters from './CustomerSearchFilters'; // 复用之前的筛选组件
import CustomerTable from './CustomerTable'; // 复用之前的表格组件
import DateFilter from './DateFilter'; // 复用日期筛选
import './CustomerList.css'; // 可复用样式

const AllCustomersList = () => {
  const [customers, setCustomers] = useState([]);
  const [filteredCustomers, setFilteredCustomers] = useState([]);
  const [filters, setFilters] = useState({
    owner: '', // 去除归属人过滤的必要性
    dataSource: '',
    studentBatch: '',
    deal7Days: false,
    deal14Days: false,
    deal21Days: false,
    searchPhone: '',
    startDate: '',
    endDate: '',
  });
  const [sort, setSort] = useState({ field: 'created_at', direction: 'desc' }); // 默认降序
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const [ownerOptions, setOwnerOptions] = useState([]);
  const [studentBatchOptions, setStudentBatchOptions] = useState([]); // 期数学员选项

  // 计算默认的3天前的日期
  const getDefaultDateRange = () => {
    const today = new Date();
    const lastThreeDays = new Date(today);
    lastThreeDays.setDate(today.getDate() - 3); // 默认加载3天前的数据
    return {
      startDate: lastThreeDays.toISOString().split('T')[0], // 格式化为 YYYY-MM-DD
      endDate: today.toISOString().split('T')[0],
    };
  };

  // 初次加载时设置默认的时间范围为3天内
  useEffect(() => {
    const { startDate, endDate } = getDefaultDateRange();
    setFilters((prev) => ({ ...prev, startDate, endDate }));
  }, []);

  // 获取客户数据
  useEffect(() => {
    fetchCustomers();
  }, [filters.startDate, filters.endDate, sort]);

  const fetchCustomers = async () => {
    try {
      setLoading(true);
      const response = await getCustomers(filters.startDate, filters.endDate, sort.field, sort.direction);

      // 筛选出符合日期范围的客户
      const filteredByDate = response.filter((customer) => {
        const customerCreatedAt = new Date(customer.created_at);
        const startDate = new Date(filters.startDate);
        const endDate = new Date(filters.endDate);
        return customerCreatedAt >= startDate && customerCreatedAt <= endDate;
      });

      setCustomers(filteredByDate);

      const owners = [...new Set(filteredByDate.map((customer) => customer.created_by))];
      setOwnerOptions(owners);

      const studentBatches = [...new Set(filteredByDate.map((customer) => customer.student_batch))].filter(Boolean);
      setStudentBatchOptions(studentBatches);

      applyFilters(filteredByDate);
    } catch (error) {
      setErrorMessage('获取客户数据时出错');
    } finally {
      setLoading(false);
    }
  };

  // 应用筛选条件
  const applyFilters = (customerList) => {
    const filtered = customerList.filter((customer) => {
      const { dataSource, studentBatch, deal7Days, deal14Days, deal21Days, searchPhone } = filters;

      return (
        (!dataSource || customer.data_source === dataSource) &&
        (!studentBatch || customer.student_batch === studentBatch) &&
        (!searchPhone || customer.phone.includes(searchPhone)) &&
        (!deal7Days || customer.deal_7_days_checked) &&
        (!deal14Days || customer.deal_14_days_checked) &&
        (!deal21Days || customer.deal_21_days_checked)
      );
    });

    setFilteredCustomers(filtered);
  };

  useEffect(() => {
    applyFilters(customers);
  }, [filters, customers]);

  // 更新筛选条件
  const handleFilterChange = (newFilters) => setFilters((prev) => ({ ...prev, ...newFilters }));

  // 处理日期选择的变化
  const handleDateChange = (startDate, endDate) => setFilters((prev) => ({ ...prev, startDate, endDate }));

  return (
    <div className="customer-list-container">
      <div className="filters-container">
        <DateFilter initialStartDate={filters.startDate} initialEndDate={filters.endDate} onDateChange={handleDateChange} />
        <CustomerSearchFilters
          filters={filters}
          onFilterChange={handleFilterChange}
          ownerOptions={ownerOptions}
          studentBatchOptions={studentBatchOptions}
        />
      </div>

      <CustomerTable
        customers={filteredCustomers}
        onDelete={() => {}} // 禁止删除，传入空函数
        currentUser={null} // 禁止编辑，传入 null，限制功能
        isViewOnly // 增加只读模式
      />

      {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}
      {loading && <div className="loading-indicator">加载中...</div>}
    </div>
  );
};

export default AllCustomersList;