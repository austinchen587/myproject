import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getCustomers, deleteCustomer } from '../api/customerApi';
import { getCurrentUser } from '../api/authApi';
import CustomerSearchFilters from './CustomerSearchFilters';
import CustomerTable from './CustomerTable';
import DateFilter from './DateFilter';
import './CustomerList.css';

// 获取最近5天的默认时间范围
const getLastFiveDays = () => {
  const today = new Date();
  const fiveDaysAgo = new Date(today);
  fiveDaysAgo.setDate(today.getDate() - 5);

  return {
    startDate: fiveDaysAgo.toISOString().split('T')[0],
    endDate: today.toISOString().split('T')[0],
  };
};

const CustomerList = () => {
  const navigate = useNavigate();
  const [customers, setCustomers] = useState([]);
  const [filteredCustomers, setFilteredCustomers] = useState([]);
  const [ownerOptions, setOwnerOptions] = useState([]);
  const [studentBatchOptions, setStudentBatchOptions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const [currentUser, setCurrentUser] = useState(null);

  const defaultDates = getLastFiveDays();
  const [filters, setFilters] = useState({
    owner: '',
    dataSource: '',
    studentBatch: '',
    deal7Days: false,
    deal14Days: false,
    deal21Days: false,
    searchPhone: '',
    startDate: defaultDates.startDate,
    endDate: defaultDates.endDate,
    filterExclamation: false,
  });

  const [sort, setSort] = useState({ field: 'created_at', direction: 'desc' });

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
  }, [currentUser, filters, sort]);

  const fetchCustomers = async () => {
    try {
      setLoading(true);
      const response = await getCustomers(filters.startDate, filters.endDate, sort.field, sort.direction);
      setCustomers(response);

      const owners = [...new Set(response.map((customer) => customer.created_by))];
      const batches = [...new Set(response.map((customer) => customer.student_batch))];

      setOwnerOptions(owners.filter(Boolean));
      setStudentBatchOptions(batches.filter(Boolean));

      applyFilters(response);
    } catch (error) {
      setErrorMessage('获取客户数据时出错');
    } finally {
      setLoading(false);
    }
  };

  const applyFilters = (customerList) => {
    const filtered = customerList.filter((customer) => {
      const {
        owner,
        dataSource,
        studentBatch,
        searchPhone,
        filterExclamation,
        deal7Days,
        deal14Days,
        deal21Days,
      } = filters;

      const hasExclamation = customer.created_by !== customer.updated_by;

      return (
        (!owner || customer.created_by === owner) &&
        (!dataSource || customer.data_source === dataSource) &&
        (!studentBatch || customer.student_batch === studentBatch) &&
        (!searchPhone || customer.phone.includes(searchPhone)) &&
        (!filterExclamation || hasExclamation) &&
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

  const handleFilterChange = (newFilters) => {
    const updatedFilters = { ...filters, ...newFilters };
    setFilters(updatedFilters);
    sessionStorage.setItem('customerListFilters', JSON.stringify(updatedFilters));
  };

  const handleDateChange = (startDate, endDate) => {
    handleFilterChange({ startDate, endDate });
  };

  return (
    <div className="customer-list-container">
      <div className="filters-container">
        <DateFilter
          initialStartDate={filters.startDate}
          initialEndDate={filters.endDate}
          onDateChange={handleDateChange}
        />
        <CustomerSearchFilters
          filters={filters}
          onFilterChange={handleFilterChange}
          ownerOptions={ownerOptions}
          studentBatchOptions={studentBatchOptions}
        />
        <div className="button-group">
          <button className="btn btn-primary" onClick={() => navigate('/add-customer')}>
            添加客户
          </button>
          <button className="btn btn-secondary" onClick={() => navigate('/all-customers')}>
            查看所有客户
          </button>
        </div>
      </div>

      <CustomerTable
        customers={filteredCustomers}
        onDelete={async (id) => {
          await deleteCustomer(id);
          fetchCustomers();
        }}
        currentUser={currentUser}
      />

      {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}
      {loading && <div className="loading-indicator">加载中...</div>}
    </div>
  );
};

export default CustomerList;