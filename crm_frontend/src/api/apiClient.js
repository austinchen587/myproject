// 这个文件负责创建一个通用的 axios 实例，用于处理所有 API 请求
import axios from 'axios';

// 创建一个 axios 实例，并配置基础 URL 和请求超时时间
const apiClient = axios.create({
    baseURL: 'http://47.96.21.74/api', // 设置后端 API 的基础 URL
    timeout: 10000, // 设置请求超时时间（可根据需求调整）
    withCredentials: true, // 允许跨域请求附带 cookie
});

// 获取 CSRF 令牌并附加到每个请求
const getCsrfToken = () => {
    const csrfToken = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    console.log('CSRF Token:', csrfToken);  // 打印 CSRF Token
    return csrfToken;
};

// 请求拦截器：自动附加 CSRF token 和 JWT token 到每个请求的头部
apiClient.interceptors.request.use(
    (config) => {
        console.log('Outgoing request:', config.url);  // 打印请求的 URL
        
        const csrfToken = getCsrfToken();
        if (csrfToken) {
            config.headers['X-CSRFToken'] = csrfToken;  // 设置 CSRF 令牌
            console.log('CSRF Token added to headers');
        }

        // 仅在非登录和刷新 token 的请求中附加 JWT token
        if (!config.url.includes('/login/') && !config.url.includes('/token/refresh/')) {
            const token = localStorage.getItem('access_token');
            console.log('Access Token from localStorage:', token);  // 打印 access token

            if (token) {
                config.headers['Authorization'] = `Bearer ${token}`; // 设置 JWT token
                console.log('Authorization header set');
            }
        }

        return config;
    },
    (error) => {
        console.error('Request error:', error);  // 打印请求错误
        return Promise.reject(error);
    }
);

// 响应拦截器：处理 401 错误并刷新 token
apiClient.interceptors.response.use(
    (response) => {
        console.log('Response received:', response);  // 打印响应
        return response;
    },
    async (error) => {
        const originalRequest = error.config;
        console.error('Response error:', error.response ? error.response.data : error.message);  // 打印响应错误

        // 如果返回 401 且没有尝试过刷新令牌
        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            console.warn('401 Unauthorized - Attempting to refresh token');

            try {
                const refreshToken = localStorage.getItem('refresh_token');
                console.log('Refresh Token from localStorage:', refreshToken);  // 打印 refresh token

                const refreshResponse = await apiClient.post('/token/refresh/', { refresh: refreshToken });
                console.log('New Access Token received:', refreshResponse.data.access);  // 打印新的 access token

                // 更新新的 access_token
                const newAccessToken = refreshResponse.data.access;
                localStorage.setItem('access_token', newAccessToken);
                originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;

                // 重新发送原来的请求
                return apiClient(originalRequest);
            } catch (err) {
                console.error('Token refresh failed:', err.response ? err.response.data : err.message);  // 打印刷新失败的错误
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                console.warn('Redirecting to login...');
                window.location.href = '/login';  // 跳转到登录页面
                return Promise.reject(err);
            }
        }

        return Promise.reject(error);
    }
);

export default apiClient;