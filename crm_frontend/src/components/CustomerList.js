import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './CustomerList.css';
import { deleteCustomer, getCustomers } from '../api/customerApi';
import { getCurrentUser } from '../api/authApi';
import DateFilter from './DateFilter';

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);
    const [sortField, setSortField] = useState('created_at');
    const [sortDirection, setSortDirection] = useState('asc');
    const [errorMessage, setErrorMessage] = useState('');
    const [loading, setLoading] = useState(true);
    const [currentUser, setCurrentUser] = useState(null);
    const [startDate, setStartDate] = useState(''); 
    const [endDate, setEndDate] = useState(''); 
    const navigate = useNavigate();

    // 获取当前用户信息
    useEffect(() => {
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

    // 获取客户列表
    useEffect(() => {
        if (currentUser) {
            fetchCustomers();
        }
    }, [currentUser, startDate, endDate, sortField, sortDirection]);

    const fetchCustomers = async () => {
        try {
            setLoading(true);
            
            // 校验时间范围
            if (startDate && endDate && new Date(endDate) < new Date(startDate)) {
                setErrorMessage('截止时间不能早于开始时间');
                setLoading(false);
                return;
            }

            // 若未选择日期，默认查询当月数据
            const start = startDate || new Date(new Date().getFullYear(), new Date().getMonth(), 1).toISOString().split('T')[0];
            const end = endDate || new Date().toISOString().split('T')[0];

            const response = await getCustomers(start, end, sortField, sortDirection);
            console.log('收到的客户数据:', response);
            setCustomers(response);
            setErrorMessage('');
        } catch (error) {
            setErrorMessage('获取客户数据时出错');
            console.error('获取客户列表时出错:', error);
        } finally {
            setLoading(false);
        }
    };

    // 处理时间变化
    const handleDateChange = (newStartDate, newEndDate) => {
        setStartDate(newStartDate);
        setEndDate(newEndDate);
    };

    // 删除客户
    const handleDelete = async (customerId) => {
        try {
            await deleteCustomer(customerId);
            fetchCustomers();
        } catch (error) {
            console.error('删除客户失败:', error);
        }
    };

    // 排序功能
    const handleSort = (field) => {
        const direction = sortField === field && sortDirection === 'asc' ? 'desc' : 'asc';
        setSortField(field);
        setSortDirection(direction);
    };

    if (loading) {
        return <div>加载中...</div>;
    }

    return (
        <div className="customer-list table-responsive">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <DateFilter onDateChange={handleDateChange} />
                <button className="btn btn-primary" onClick={() => navigate('/add-customer')}>
                    添加客户
                </button>
            </div>
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
                    {customers.length > 0 ? (
                        customers.map((customer) => (
                            <tr key={customer.id}>
                                <td>{customer.name}</td>
                                <td>{customer.phone}</td>
                                <td>{new Date(customer.created_at).toLocaleDateString()}</td>
                                <td>{customer.created_by}</td>
                                <td>{customer.intention}</td>
                                <td>{customer.is_invited ? '是' : '否'}</td>
                                <td>{customer.is_joined ? '是' : '否'}</td>
                                <td>{customer.attended_first_live ? '是' : '否'}</td>
                                <td>{customer.attended_second_live ? '是' : '否'}</td>
                                <td>{customer.is_closed ? '是' : '否'}</td>
                                <td>
                                    <Link to={`/customer/${customer.id}`} className="btn btn-info btn-sm mr-2">
                                        详情
                                    </Link>
                                    <Link to={`/edit-customer/${customer.id}`} className="btn btn-warning btn-sm mr-2">
                                        更新
                                    </Link>
                                    {currentUser && (currentUser.role === 'admin' || currentUser.role === 'group_leader') && (
                                        <button onClick={() => handleDelete(customer.id)} className="btn btn-danger btn-sm">
                                            删除
                                        </button>
                                    )}
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

            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
        </div>
    );
};

export default CustomerList;