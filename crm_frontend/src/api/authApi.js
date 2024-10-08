// 这个文件专门处理用户登录相关的 API 调用
import apiClient from './apiClient'; // 导入配置好的 axios 实例

export const loginUser = async (credentials) => {
    try {
        const response = await apiClient.post('login/', credentials);
        
        // 打印后端返回的数据
        console.log('Response Data:', response.data);
        
        // 确保从 response.data 中获取正确的 token 字段
        const { access_token, refresh_token } = response.data;
        
        // 打印 token 信息，帮助调试
        console.log('Access Token:', access_token);
        console.log('Refresh Token:', refresh_token);
        
        // 存储 token
        localStorage.setItem('access_token', access_token);  // 存储访问 token
        localStorage.setItem('refresh_token', refresh_token);  // 存储刷新 token
        
        // 检查 token 是否存储成功
        console.log('Stored Access Token:', localStorage.getItem('access_token'));
        console.log('Stored Refresh Token:', localStorage.getItem('refresh_token'));
        
        return response.data; // 返回 token 或者其他登录信息
    } catch (error) {
        // 打印错误信息
        console.error('Login failed:', error.response ? error.response.data : error.message);
        throw error;
    }
};

// 示例：调用登录函数
loginUser({
    username: 'your_username',
    password: 'your_password'
}).then(data => {
    console.log('Login successful:', data); // 登录成功，打印返回的数据
}).catch(error => {
    console.error('Error during login:', error); // 捕捉并处理错误
});



// 获取当前登录用户信息
export const getCurrentUser = async () => {
    const accessToken = localStorage.getItem('access_token');  // 确保从本地存储中获取 access_token
    try {
      // 获取当前登录用户时，确保包含 Authorization 头
      const response = await apiClient.get('/current-user/', {
        headers: {
          Authorization: `Bearer ${accessToken}`  // 从 localStorage 中获取 access_token
        }
      });
      return response.data;
    } catch (error) {
      console.error('获取当前用户失败:', error);
      throw error;
    }
  };


  export const registerUser = async (userData) => {
    console.log('发送注册请求数据:', userData);
    const response = await apiClient.post(`/register/`, userData);
    console.log('注册请求响应:', response.data);
    return response.data;
  };