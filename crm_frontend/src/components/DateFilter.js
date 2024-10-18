// src/components/DateFilter.js
import React, { useState, useEffect } from 'react';
import './DateFilter.css'; // 引入样式文件

const DateFilter = ({ initialStartDate, initialEndDate, onDateChange }) => {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');

    useEffect(() => {
        // 初始化日期字段
        if (initialStartDate) setStartDate(initialStartDate);
        if (initialEndDate) setEndDate(initialEndDate);
    }, [initialStartDate, initialEndDate]);

    const handleStartDateChange = (e) => {
        const newStartDate = e.target.value;
        setStartDate(newStartDate);
        onDateChange(newStartDate || '', endDate || ''); // 避免传递 undefined
    };

    const handleEndDateChange = (e) => {
        const newEndDate = e.target.value;
        setEndDate(newEndDate);
        onDateChange(startDate || '', newEndDate || ''); // 避免传递 undefined
    };

    return (
        <div className="date-filter-container">
            <div className="date-input-group">
                <label htmlFor="start-date" className="date-label">开始日期</label>
                <input
                    type="date"
                    id="start-date"
                    value={startDate}
                    onChange={handleStartDateChange}
                    className="form-control date-input-field"
                />
            </div>
            <div className="date-input-group">
                <label htmlFor="end-date" className="date-label">结束日期</label>
                <input
                    type="date"
                    id="end-date"
                    value={endDate}
                    onChange={handleEndDateChange}
                    className="form-control date-input-field"
                />
            </div>
        </div>
    );
};

export default DateFilter;