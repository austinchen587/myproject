import React, { useState } from 'react';
import { loginUser, getCurrentUser } from '../api/authApi'; 
import LoginForm from './LoginForm'; 
import { useNavigate } from 'react-router-dom';
import './Login.css'; 

const Login = ({ setCurrentUser }) => {
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (credentials) => {
        if (!credentials.username || !credentials.password) {
            setMessage('用户名和密码不能为空');
            return;
        }

        try {
            const data = await loginUser(credentials);
            setMessage('登录成功');

            const user = await getCurrentUser();
            setCurrentUser(user);

            navigate('/customers');
        } catch (error) {
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