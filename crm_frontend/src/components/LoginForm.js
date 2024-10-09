import React, { useState } from 'react';
import './LoginForm.css'; // 确保引入了上面的 CSS 文件

const LoginForm = ({ onLogin }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onLogin({ username, password });
    };

    return (
        <form onSubmit={handleSubmit} className="formlogin">
            <div>
                <label>用户名:</label>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
            </div>
            <div>
                <label>密码:</label>
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button type="submit">登录</button>
        </form>
    );
};

export default LoginForm;