// 这个文件专门处理用户登录相关的 API 调用
import apiClient from './apiClient'; // 导入配置好的 axios 实例

// 登录用户并存储 access_token 和 refresh_token
export const loginUser = async (credentials) => {
  try {
      const response = await apiClient.post('login/', credentials);

      // 从响应中获取令牌
      const { access_token, refresh_token } = response.data;
      if (!access_token || !refresh_token) {
          throw new Error('Missing tokens in the response.');
      }

      // 存储令牌到 localStorage
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_token);

      return response.data; // 返回响应数据
  } catch (error) {
      // 捕获错误并返回给调用者
      console.error('登录失败:', error.response ? error.response.data : error.message);
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



// 获取当前用户信息
export const getCurrentUser = async () => {
  const accessToken = localStorage.getItem('access_token');
  
  if (!accessToken) {
      // 如果没有 access_token，直接引导用户重新登录
      console.error('Access token missing. Redirecting to login.');
      window.location.href = '/login';
      return;
  }

  try {
      // 使用 access_token 获取当前登录用户信息
      const response = await apiClient.get('/current-user/', {
          headers: {
              Authorization: `Bearer ${accessToken}`
          }
      });
      return response.data;
  } catch (error) {
      console.error('Failed to fetch current user:', error);

      // 清除过期令牌并引导用户登录
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      window.location.href = '/login';
      throw error;
  }
};


  export const registerUser = async (userData) => {
    console.log('发送注册请求数据:', userData);
    const response = await apiClient.post(`/register/`, userData);
    console.log('注册请求响应:', response.data);
    return response.data;
  };