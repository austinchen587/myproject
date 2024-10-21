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
  const [ownerOptions, setOwnerOptions] = useState([]);
  const [studentBatchOptions, setStudentBatchOptions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const [currentUser, setCurrentUser] = useState(null);
  const navigate = useNavigate();

  const [filters, setFilters] = useState(() => {
    const savedFilters = sessionStorage.getItem('customerListFilters');
    return savedFilters ? JSON.parse(savedFilters) : {
      owner: '',
      dataSource: '',
      studentBatch: '',
      deal7Days: false,
      deal14Days: false,
      deal21Days: false,
      searchPhone: '',
      startDate: '',
      endDate: '',
      filterExclamation: false,
    };
  });

  const [sort, setSort] = useState(() => {
    const savedSort = sessionStorage.getItem('customerListSort');
    return savedSort ? JSON.parse(savedSort) : { field: 'created_at', direction: 'desc' };
  });

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

      // 提取归属人和期数学员选项
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
      const { owner, dataSource, studentBatch, searchPhone, filterExclamation } = filters;
      const hasExclamation = customer.created_by !== customer.updated_by;

      return (
        (!owner || customer.created_by === owner) &&
        (!dataSource || customer.data_source === dataSource) &&
        (!studentBatch || customer.student_batch === studentBatch) &&
        (!searchPhone || customer.phone.includes(searchPhone)) &&
        (!filterExclamation || hasExclamation)
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