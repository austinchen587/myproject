import React from 'react';
import AppRoutes from './routes/AppRoutes'; // 引入路由组件



// App.js 只负责渲染主要的应用内容和路由组件
const App = () => {
    
    return (
        <div>
          
            <AppRoutes /> {/* 这里加载所有的路由 */}
        </div>
    );
};

export default App;