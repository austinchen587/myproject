document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggle-filter');
    const filterForm = document.getElementById('filter-form');

    // 检查是否找到 DOM 元素
    if (toggleButton && filterForm) {
        toggleButton.addEventListener('click', function () {
            // 切换表单的显示状态
            if (filterForm.style.display === 'none' || filterForm.style.display === '') {
                filterForm.style.display = 'block';
                toggleButton.textContent = '隐藏筛选条件';
            } else {
                filterForm.style.display = 'none';
                toggleButton.textContent = '显示筛选条件';
            }
        });
    } else {
        console.error('筛选按钮或筛选表单未找到！');
    }
});