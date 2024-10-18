import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // 引入自定义样式
import 'bootstrap/dist/css/bootstrap.min.css'; // 引入 Bootstrap

const Home = () => {
  return (
    <div className="home-container d-flex align-items-center justify-content-center vh-100">
      <div className="text-center">
        <h1 className="display-4">欢迎来传知摩尔狮-南昌-CRM-系统</h1>
        <p className="lead">努力工作 开心生活</p>
        <div className="mt-5">
          <Link to="/login" className="btn btn-primary btn-lg mr-3">登录</Link>
        </div>
      </div>
    </div>
  );
};

export default Home;