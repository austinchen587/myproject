// src/components/IntentionFilter.js
import React from 'react';
import './IntentionFilter.css';

const IntentionFilter = ({ selectedIntention, onSelectIntention }) => {
    const intentions = ['所有意向', '高', '中', '低'];

    const handleChange = (e) => {
        onSelectIntention(e.target.value);
    };

    return (
        <div className="intention-filter">
            <label htmlFor="intention-select" className="intention-filter-label">
                筛选意向程度：
            </label>
            <select
                id="intention-select"
                className="form-control intention-select"
                value={selectedIntention}
                onChange={handleChange}
            >
                {intentions.map((intention, index) => (
                    <option key={index} value={intention === '所有意向' ? '' : intention}>
                        {intention}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default IntentionFilter;