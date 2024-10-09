// src/components/DateFilter.js
import React, { useState, useEffect } from 'react';
import './DateFilter.css';

const DateFilter = ({ initialStartDate, initialEndDate, onDateChange }) => {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');

    useEffect(() => {
        // 设置初始日期
        if (initialStartDate) {
            setStartDate(initialStartDate);
        }
        if (initialEndDate) {
            setEndDate(initialEndDate);
        }
    }, [initialStartDate, initialEndDate]);

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
        <div className="date-filter">
            <div className="date-input">
                <label htmlFor="start-date" className="date-label">开始日期</label>
                <input
                    type="date"
                    id="start-date"
                    value={startDate}
                    onChange={handleStartDateChange}
                    className="form-control date-input-field"
                />
            </div>
            <div className="date-input">
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