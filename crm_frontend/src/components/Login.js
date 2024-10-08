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
        try {
            const data = await loginUser(credentials); // 发送登录请求
            setMessage('登录成功');

            // 确保 token 已存储后再调用 getCurrentUser
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);            

            console.log('Access Token:', localStorage.getItem('access_token')); // 检查获取到的 access_token

            // 获取当前用户信息
            const user = await getCurrentUser();
            setCurrentUser(user); // 更新当前用户信息

            // 跳转到客户列表页面
            navigate('/customers');
        } catch (error) {
            setMessage('登录失败，请检查用户名和密码');
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