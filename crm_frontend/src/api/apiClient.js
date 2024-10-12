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
    return csrfToken;
};

// 请求拦截器：自动附加 CSRF token 和 JWT token 到每个请求的头部
apiClient.interceptors.request.use(
    (config) => {
        const csrfToken = getCsrfToken();
        if (csrfToken) {
            config.headers['X-CSRFToken'] = csrfToken;  // 设置 CSRF 令牌
        }

        // 仅在非登录和刷新 token 的请求中附加 JWT token
        if (!config.url.includes('/login/') && !config.url.includes('/token/refresh/')) {
            const token = localStorage.getItem('access_token');
            if (token) {
                config.headers['Authorization'] = `Bearer ${token}`; // 设置 JWT token
            }
        }

        return config;
    },
    (error) => Promise.reject(error)
);

apiClient.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        // 如果返回 401 且没有尝试过刷新令牌
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;

            try {
                // 获取 refresh_token
                const refreshToken = localStorage.getItem('refresh_token');

                // 检查 refresh_token 是否存在
                if (!refreshToken) {
                    console.error('Refresh token is missing. Redirecting to login.');
                    window.location.href = '/login'; // 跳转到登录页面
                    return Promise.reject(error);
                }

                // 尝试刷新 token
                const refreshResponse = await apiClient.post('/token/refresh/', { refresh: refreshToken });
                const newAccessToken = refreshResponse.data.access;

                // 更新新的 access_token
                localStorage.setItem('access_token', newAccessToken);
                originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;

                // 重新发送原来的请求
                return apiClient(originalRequest);
            } catch (err) {
                console.error('Token refresh failed:', err);

                // 清除过期的令牌，避免无限循环
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');

                // 跳转到登录页面
                window.location.href = '/login';
                return Promise.reject(err);
            }
        }

        // 返回其他错误
        return Promise.reject(error);
    }
);




export default apiClient;
