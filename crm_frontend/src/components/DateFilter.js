import React from 'react';

const DateFilter = ({ onDateChange, startDate, endDate }) => {
    const handleStartDateChange = (e) => {
        onDateChange(e.target.value, endDate);
    };

    const handleEndDateChange = (e) => {
        onDateChange(startDate, e.target.value);
    };

    return (
        <div className="date-filter">
            <label>开始时间: </label>
            <input
                type="date"
                value={startDate}
                onChange={handleStartDateChange}
                className="form-control d-inline w-auto"
            />
            <label>截止时间: </label>
            <input
                type="date"
                value={endDate}
                onChange={handleEndDateChange}
                className="form-control d-inline w-auto"
            />
        </div>
    );
};

export default DateFilter;