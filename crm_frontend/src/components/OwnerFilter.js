import React, { useEffect, useState } from 'react';
import './OwnerFilter.css';

const OwnerFilter = ({ owners, selectedOwner, onSelectOwner }) => {
    const [availableOwners, setAvailableOwners] = useState([]);

    useEffect(() => {
        // 根据传入的客户列表提取归属人选项
        if (owners) {
            const uniqueOwners = [...new Set(owners)];
            setAvailableOwners(uniqueOwners);
        }
    }, [owners]);

    const handleChange = (e) => {
        onSelectOwner(e.target.value);
    };

    return (
        <div className="owner-filter">
            <label htmlFor="owner-select" className="owner-filter-label">筛选归属人：</label>
            <select
                id="owner-select"
                className="owner-filter-select"
                value={selectedOwner}
                onChange={handleChange}
            >
                <option value="">所有归属人</option>
                {availableOwners.map((owner, index) => (
                    <option key={index} value={owner}>
                        {owner}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default OwnerFilter;