import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getCustomers, deleteCustomer } from '../api/customerApi';
import { getCurrentUser } from '../api/authApi';
import CustomerSearchFilters from './CustomerSearchFilters';
import CustomerTable from './CustomerTable';
import DateFilter from './DateFilter';
import './CustomerList.css';

const CustomerList = () => {
  const [customers, setCustomers] = useState([]);
  const [filteredCustomers, setFilteredCustomers] = useState([]);
  const [filters, setFilters] = useState({
    owner: '',
    dataSource: '',
    studentBatch: '',
    deal7Days: false,
    deal14Days: false,
    deal21Days: false,
    searchPhone: '',
    startDate: '',  // 默认一周前的开始日期
    endDate: '',    // 默认今天的结束日期
  });
  const [sort, setSort] = useState({ field: 'created_at', direction: 'desc' }); // 默认降序
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const [currentUser, setCurrentUser] = useState(null);
  const [ownerOptions, setOwnerOptions] = useState([]);
  const [studentBatchOptions, setStudentBatchOptions] = useState([]); // 期数学员选项
  const navigate = useNavigate();

  // 计算默认的一周前的日期
  const getDefaultDateRange = () => {
    const today = new Date();
    const lastWeek = new Date(today);
    lastWeek.setDate(today.getDate() - 7); // 获取一周前的日期
    return {
      startDate: lastWeek.toISOString().split('T')[0], // 转化为 YYYY-MM-DD 格式
      endDate: today.toISOString().split('T')[0],      // 转化为 YYYY-MM-DD 格式
    };
  };

  // 初次加载时设置默认日期
  useEffect(() => {
    const { startDate, endDate } = getDefaultDateRange();
    setFilters((prev) => ({ ...prev, startDate, endDate }));
  }, []);

  // 获取当前用户信息
  useEffect(() => {
    const fetchUser = async () => {
      try {
        const user = await getCurrentUser();
        setCurrentUser(user);
      } catch (error) {
        console.error('获取用户信息失败:', error);
      }
    };
    fetchUser();
  }, []);

  // 获取客户数据
  useEffect(() => {
    if (currentUser) fetchCustomers();
  }, [currentUser, filters.startDate, filters.endDate, sort]);

  const fetchCustomers = async () => {
    try {
      setLoading(true);
      const response = await getCustomers(filters.startDate, filters.endDate, sort.field, sort.direction);
      setCustomers(response);

      const owners = [...new Set(response.map((customer) => customer.created_by))];
      setOwnerOptions(owners);

      const studentBatches = [...new Set(response.map((customer) => customer.student_batch))].filter(Boolean); // 获取学员期数选项
      setStudentBatchOptions(studentBatches);

      applyFilters(response);
    } catch (error) {
      setErrorMessage('获取客户数据时出错');
    } finally {
      setLoading(false);
    }
  };

  const applyFilters = (customerList) => {
    const filtered = customerList.filter((customer) => {
      const { owner, dataSource, studentBatch, deal7Days, deal14Days, deal21Days, searchPhone } = filters;

      return (
        (!owner || customer.created_by === owner) &&
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

  const handleDelete = async (id) => {
    try {
      await deleteCustomer(id);
      fetchCustomers();
    } catch (error) {
      console.error('删除客户失败:', error);
    }
  };

  const handleFilterChange = (newFilters) => setFilters((prev) => ({ ...prev, ...newFilters }));
  const handleDateChange = (startDate, endDate) => setFilters((prev) => ({ ...prev, startDate, endDate }));

  return (
    <div className="customer-list-container">
      <div className="filters-container">
        <DateFilter initialStartDate={filters.startDate} initialEndDate={filters.endDate} onDateChange={handleDateChange} />
        <CustomerSearchFilters
          filters={filters}
          onFilterChange={handleFilterChange}
          ownerOptions={ownerOptions}
          studentBatchOptions={studentBatchOptions} // 传递学员期数选项
        />
        <button className="btn btn-primary add-customer-btn" onClick={() => navigate('/add-customer')}>
          添加客户
        </button>
      </div>

      <CustomerTable customers={filteredCustomers} onDelete={handleDelete} currentUser={currentUser} />

      {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}
      {loading && <div className="loading-indicator">加载中...</div>}
    </div>
  );
};

export default CustomerList;