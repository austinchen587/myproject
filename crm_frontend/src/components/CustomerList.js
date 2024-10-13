import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './CustomerList.css'; // 使用局部样式
import { deleteCustomer, getCustomers } from '../api/customerApi';
import { getCurrentUser } from '../api/authApi';
import DateFilter from './DateFilter';
import OwnerFilter from './OwnerFilter';
import IntentionFilter from './IntentionFilter';
import { FaCheckCircle, FaTimesCircle, FaArrowUp, FaArrowDown, FaExclamationCircle } from 'react-icons/fa'; // 导入感叹号图标

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);
    const [sortField, setSortField] = useState('created_at');
    const [sortDirection, setSortDirection] = useState('asc');
    const [errorMessage, setErrorMessage] = useState('');
    const [loading, setLoading] = useState(true);
    const [currentUser, setCurrentUser] = useState(null);
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [selectedOwner, setSelectedOwner] = useState('');
    const [selectedIntention, setSelectedIntention] = useState('');
    const [filterExclamation, setFilterExclamation] = useState(false); // 用于感叹号筛选
    const [searchPhone, setSearchPhone] = useState(''); // 用于手机号筛选
    const [phoneInput, setPhoneInput] = useState(''); // 用户输入的手机号
    const navigate = useNavigate();

    useEffect(() => {
        const savedStartDate = localStorage.getItem('startDate');
        const savedEndDate = localStorage.getItem('endDate');
        const savedOwner = localStorage.getItem('selectedOwner');
        const savedIntention = localStorage.getItem('selectedIntention');
        const savedFilterExclamation = localStorage.getItem('filterExclamation') === 'true';
        const savedSearchPhone = localStorage.getItem('searchPhone') || '';

        if (savedStartDate) setStartDate(savedStartDate);
        if (savedEndDate) setEndDate(savedEndDate);
        if (savedOwner) setSelectedOwner(savedOwner);
        if (savedIntention) setSelectedIntention(savedIntention);
        setFilterExclamation(savedFilterExclamation);
        setSearchPhone(savedSearchPhone);

        const fetchUser = async () => {
            try {
                const user = await getCurrentUser();
                setCurrentUser(user);
            } catch (error) {
                console.error('获取用户信息失败', error);
            }
        };
        fetchUser();
    }, []);

    useEffect(() => {
        localStorage.setItem('startDate', startDate);
        localStorage.setItem('endDate', endDate);
        localStorage.setItem('selectedOwner', selectedOwner);
        localStorage.setItem('selectedIntention', selectedIntention);
        localStorage.setItem('filterExclamation', filterExclamation);
        localStorage.setItem('searchPhone', searchPhone); // 存储手机号筛选
    }, [startDate, endDate, selectedOwner, selectedIntention, filterExclamation, searchPhone]);

    useEffect(() => {
        if (currentUser) {
            fetchCustomers();
        }
    }, [currentUser, startDate, endDate, sortField, sortDirection, filterExclamation, searchPhone]);

    const fetchCustomers = async () => {
        try {
            setLoading(true);

            if (startDate && endDate && new Date(endDate) < new Date(startDate)) {
                setErrorMessage('截止时间不能早于开始时间');
                setLoading(false);
                return;
            }

            const start = startDate || new Date(new Date().getFullYear(), new Date().getMonth(), 1).toISOString().split('T')[0];
            const end = endDate || new Date().toISOString().split('T')[0];

            const response = await getCustomers(start, end, sortField, sortDirection);
            setCustomers(response);
            setErrorMessage('');
        } catch (error) {
            setErrorMessage('获取客户数据时出错');
            console.error('获取客户列表时出错:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleDateChange = (newStartDate, newEndDate) => {
        setStartDate(newStartDate);
        setEndDate(newEndDate);
    };

    const handleOwnerSelect = (owner) => {
        setSelectedOwner(owner);
    };

    const handleIntentionSelect = (intention) => {
        setSelectedIntention(intention);
    };

    const handleExclamationFilter = (event) => {
        setFilterExclamation(event.target.checked);
    };

    const handlePhoneInputChange = (event) => {
        setPhoneInput(event.target.value);
    };

    const handlePhoneSearch = () => {
        setSearchPhone(phoneInput); // 点击按钮后执行手机号筛选
    };

    const filteredCustomers = customers
        .filter((customer) => (selectedOwner ? customer.created_by === selectedOwner : true))
        .filter((customer) => (selectedIntention ? customer.intention === selectedIntention : true))
        .filter((customer) => (filterExclamation ? customer.created_by !== customer.updated_by : true)) // 筛选带感叹号的客户
        .filter((customer) => (searchPhone ? customer.phone.includes(searchPhone) : true)); // 筛选符合手机号的客户

    const handleSort = (field) => {
        const direction = sortField === field && sortDirection === 'asc' ? 'desc' : 'asc';
        setSortField(field);
        setSortDirection(direction);
    };

    const handleDelete = async (customerId) => {
        try {
            await deleteCustomer(customerId);
            fetchCustomers();
        } catch (error) {
            console.error('删除客户失败:', error);
        }
    };

    if (loading) {
        return (
            <div className="loading-indicator">
                <div className="spinner-border text-primary" role="status">
                    <span className="sr-only">加载中...</span>
                </div>
            </div>
        );
    }

    return (
        <div className="customer-list-container">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <DateFilter
                    initialStartDate={startDate}
                    initialEndDate={endDate}
                    onDateChange={handleDateChange}
                />
                <OwnerFilter
                    owners={customers.map((customer) => customer.created_by)}
                    selectedOwner={selectedOwner}
                    onSelectOwner={handleOwnerSelect}
                />
                <IntentionFilter
                    selectedIntention={selectedIntention}
                    onSelectIntention={handleIntentionSelect}
                />

                {/* 新增的感叹号筛选复选框 */}
                <div className="form-check ml-3">
                    <input
                        className="form-check-input"
                        type="checkbox"
                        checked={filterExclamation}
                        onChange={handleExclamationFilter}
                    />
                    <label className="form-check-label">
                        只显示名字带感叹号的客户
                    </label>
                </div>

                {/* 新增手机号筛选 */}
                <div className="ml-3">
                    <label>输入手机号筛选：</label>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="输入手机号"
                        value={phoneInput}
                        onChange={handlePhoneInputChange}
                    />
                    <button className="btn btn-primary mt-2" onClick={handlePhoneSearch}>
                        确定
                    </button>
                </div>

                <button
                    className="btn btn-secondary ml-2"
                    onClick={() => navigate('/customer-analysis', { state: { currentUser } })}
                >
                    分析数据
                </button>

                <button className="btn btn-primary ml-2" onClick={() => navigate('/add-customer')}>
                    添加客户
                </button>
            </div>
            <div className="table-container">
                <table className="table table-bordered table-striped">
                    <thead className="thead-dark">
                        <tr>
                            <th onClick={() => handleSort('name')}>姓名</th>
                            <th onClick={() => handleSort('phone')}>电话</th>
                            <th onClick={() => handleSort('created_at')}>创建时间</th>
                            <th onClick={() => handleSort('created_by')}>归属人</th>
                            <th onClick={() => handleSort('intention')}>意向程度</th>
                            <th>是否邀约</th>
                            <th>是否入群</th>
                            <th>参加第一天直播</th>
                            <th>参加第二天直播</th>
                            <th>是否成交</th>
                            <th>操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredCustomers.length > 0 ? (
                            filteredCustomers.map((customer) => (
                                <tr key={customer.id}>
                                    <td>
                                        {customer.name}{' '}
                                        {customer.created_by !== customer.updated_by && (
                                            <FaExclamationCircle className="text-danger" />
                                        )}
                                    </td>
                                    <td>{customer.phone}</td>
                                    <td>{new Date(customer.created_at).toLocaleDateString()}</td>
                                    <td>{customer.created_by}</td>
                                    <td>
                                        {customer.intention === '高' && <FaArrowUp className="text-success" />}
                                        {customer.intention === '中' && <FaArrowDown className="text-warning" />}
                                        {customer.intention === '低' && <FaArrowDown className="text-danger" />}
                                    </td>
                                    <td>
                                        {customer.is_invited ? (
                                            <FaCheckCircle className="text-success" />
                                        ) : (
                                            <FaTimesCircle className="text-danger" />
                                        )}
                                    </td>
                                    <td>
                                        {customer.is_joined ? (
                                            <FaCheckCircle className="text-success" />
                                        ) : (
                                            <FaTimesCircle className="text-danger" />
                                        )}
                                    </td>
                                    <td>
                                        {customer.attended_first_live ? (
                                            <FaCheckCircle className="text-success" />
                                        ) : (
                                            <FaTimesCircle className="text-danger" />
                                        )}
                                    </td>
                                    <td>
                                        {customer.attended_second_live ? (
                                            <FaCheckCircle className="text-success" />
                                        ) : (
                                            <FaTimesCircle className="text-danger" />
                                        )}
                                    </td>
                                    <td>
                                        {customer.is_closed ? (
                                            <FaCheckCircle className="text-success" />
                                        ) : (
                                            <FaTimesCircle className="text-danger" />
                                        )}
                                    </td>
                                    <td>
                                        <div className="btn-group">
                                            <Link to={`/customer/${customer.id}`} className="btn btn-info btn-sm">
                                                详情
                                            </Link>
                                            <Link to={`/edit-customer/${customer.id}`} className="btn btn-warning btn-sm">
                                                更新
                                            </Link>
                                            {currentUser && (currentUser.role === 'admin' || currentUser.role === 'group_leader') && (
                                                <button onClick={() => handleDelete(customer.id)} className="btn btn-danger btn-sm">
                                                    删除
                                                </button>
                                            )}
                                        </div>
                                    </td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="11" className="text-center">
                                    当前没有客户信息。
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>

            {errorMessage && <div className="alert alert-danger mt-3">{errorMessage}</div>}
        </div>
    );
};

export default CustomerList;