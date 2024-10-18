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
    startDate: '',
    endDate: '',
  });
  const [sort, setSort] = useState({ field: 'created_at', direction: 'asc' });
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const [currentUser, setCurrentUser] = useState(null);
  const [ownerOptions, setOwnerOptions] = useState([]);
  const [studentBatchOptions, setStudentBatchOptions] = useState([]); // 期数学员选项
  const navigate = useNavigate();

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

  useEffect(() => {
    if (currentUser) fetchCustomers();
  }, [currentUser, sort]);

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