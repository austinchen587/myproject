import React, { useState } from 'react';
import { loginUser, getCurrentUser } from '../api/authApi'; // 引入登录和获取用户信息的函数
import LoginForm from './LoginForm'; // 引入登录表单组件
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = ({ setCurrentUser }) => {
    const [message, setMessage] = useState(''); // 显示登录信息
    const navigate = useNavigate();

    // 处理登录逻辑
    const handleLogin = async (credentials) => {
        // 简单前端校验，确保用户名和密码不为空
        if (!credentials.username || !credentials.password) {
            setMessage('用户名和密码不能为空');
            return;
        }

        try {
            // 调用 loginUser 函数进行登录
            const data = await loginUser(credentials);
            setMessage('登录成功');

            // 获取当前用户信息并更新到父组件
            const user = await getCurrentUser();
            setCurrentUser(user);

            // 跳转到客户列表页面
            navigate('/customers');
        } catch (error) {
            // 根据错误响应，显示相应的错误消息
            if (error.response && error.response.data) {
                setMessage(`登录失败: ${error.response.data.detail || '请检查用户名和密码'}`);
            } else {
                setMessage('登录失败，网络连接错误');
            }
            console.error('登录出错:', error);
        }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <h2 className="login-title">用户登录</h2>
                <LoginForm onLogin={handleLogin} />
                {message && <p className="login-message">{message}</p>}
            </div>
        </div>
    );
};

export default Login;