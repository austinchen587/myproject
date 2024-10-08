import React, { useEffect } from 'react';

const WebSocketComponent = () => {
    useEffect(() => {
        const ws = new WebSocket('ws://47.96.21.74:9000/ws/');

        ws.onopen = () => {
            console.log('WebSocket connection established');
            ws.send('Hello Server!');
        };

        ws.onmessage = (event) => {
            console.log('Message from server: ', event.data);
        };

        ws.onclose = () => {
            console.log('WebSocket connection closed');
        };

        ws.onerror = (error) => {
            console.error('WebSocket error: ', error);
        };

        return () => {
            ws.close(); // 在组件卸载时关闭 WebSocket 连接
        };
    }, []);

    return (
        <div>
            <h1>阿里云 摩尔狮</h1>
        </div>
    );
};

export default WebSocketComponent;