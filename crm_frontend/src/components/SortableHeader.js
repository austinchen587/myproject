import React from 'react';
import './SortableHeader.css';

const SortableHeader = ({ field, label, sortField, sortDirection, onSort }) => {
    const isActive = sortField === field;
    const directionIcon = isActive ? (sortDirection === 'asc' ? '▲' : '▼') : '';

    return (
        <th
            onClick={() => onSort(field)}
            className={`sortable-header ${isActive ? 'active' : ''}`}
            style={{ cursor: 'pointer' }}
        >
            {label} <span className="direction-icon">{directionIcon}</span>
        </th>
    );
};

export default SortableHeader;