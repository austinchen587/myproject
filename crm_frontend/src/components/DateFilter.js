import React, { useState, useEffect } from 'react';
import './DateFilter.css';

const DateFilter = ({ initialStartDate, initialEndDate, onDateChange }) => {
  const [startDate, setStartDate] = useState(initialStartDate);
  const [endDate, setEndDate] = useState(initialEndDate);

  const handleStartDateChange = (e) => {
    const newStartDate = e.target.value;
    setStartDate(newStartDate);
    onDateChange(newStartDate, endDate);
  };

  const handleEndDateChange = (e) => {
    const newEndDate = e.target.value;
    setEndDate(newEndDate);
    onDateChange(startDate, newEndDate);
  };

  return (
    <div className="date-filter-container">
      <input type="date" value={startDate} onChange={handleStartDateChange} />
      <input type="date" value={endDate} onChange={handleEndDateChange} />
    </div>
  );
};

export default DateFilter;