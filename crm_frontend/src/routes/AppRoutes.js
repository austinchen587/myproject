import React, { useState }  from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from '../components/Login'; // 引入登录组件
import CustomerList from '../components/CustomerList';
import AddCustomer from '../components/AddCustomer';
import CustomerDetail from '../components/CustomerDetail';
import EditCustomer from '../components/EditCustomer';
import Home from '../components/Home';
import RegisterUser from '../components/Register';


const AppRoutes = () => {
    const [currentUser, setCurrentUser] = useState(null); // 定义当前用户状态


    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login setCurrentUser={setCurrentUser} />} />
                <Route path="/customers" element={<CustomerList currentUser={currentUser} />} />
                <Route path="/add-customer" element={<AddCustomer currentUser={currentUser} />} />  {/* 添加客户页面 */}
                <Route path="/customer/:id" element={<CustomerDetail currentUser={currentUser} />} />  {/* 客户详情路由 */}
                <Route path="/edit-customer/:id" element={<EditCustomer currentUser={currentUser} />} />  {/* 添加编辑客户的路由 */}
                {/* 可以添加更多路由 */}
            </Routes>
        </Router>
    );
};

export default AppRoutes;