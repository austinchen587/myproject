// src/api/customerApi.js
import apiClient from './apiClient';

export const getCustomers = async (startDate, endDate, sortField = 'created_at', sortDirection = 'asc') => {
  try {
    const response = await apiClient.get('customers/', {    //这是一个关键点
      params: {
        start_date: startDate || '',  // 传递空字符串，如果没有值
        end_date: endDate || '',
        sort_field: sortField,
        sort_direction: sortDirection,
      },
    });

    return response.data;
  } catch (error) {
    console.error('获取客户列表时出错:', error);
    throw error;
  }
};

export const addCustomer = async (customerData) => {
  try {
    const response = await apiClient.post('/add/', customerData);  // 确保使用 POST 方法
    console.log('客户添加成功:', response.data);
    return response.data;
  } catch (error) {
    console.error('添加客户失败:', error.response ? error.response.data : error.message);  // 打印详细错误信息
    throw error;
  }
};
``
// 删除客户
export const deleteCustomer = async (customerId) => {
  const response = await apiClient.delete(`customers/${customerId}/`);
  console.log('客户删除成功:', response.data);
  return response.data;
};

// 获取单个客户信息
export const getCustomerById = async (id) => {
  const response = await apiClient.get(`customers/${id}/`);
  return response.data;
};

// 更新客户信息
export const updateCustomer = async (id, customerData) => {
  const response = await apiClient.put(`customers/${id}/`, customerData);
  console.log('客户更新成功:', response.data);
  return response.data;
};