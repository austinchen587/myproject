import React from 'react';
import DateFilter from './DateFilter';
import CustomerSearchFilters from './CustomerSearchFilters';

const CustomerFilters = ({ filters, onFilterChange, navigate }) => {
  return (
    <div className="customer-filters d-flex justify-content-between align-items-center mb-3">
      <DateFilter
        initialStartDate={filters.startDate}
        initialEndDate={filters.endDate}
        onDateChange={(startDate, endDate) => onFilterChange({ startDate, endDate })}
      />
      <CustomerSearchFilters
        filters={filters}
        onFilterChange={onFilterChange}
      />
      <button className="btn btn-secondary ml-2" onClick={() => navigate('/customer-analysis')}>
        分析数据
      </button>
      <button className="btn btn-primary ml-2" onClick={() => navigate('/add-customer')}>
        添加客户
      </button>
    </div>
  );
};

export default CustomerFilters;