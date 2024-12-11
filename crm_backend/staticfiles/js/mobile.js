document.addEventListener("DOMContentLoaded", () => {
    // 切换客户详情显示/隐藏
    document.querySelectorAll(".toggle-details").forEach(button => {
        button.addEventListener("click", () => {
            const details = button.previousElementSibling;
            const isHidden = details.style.display === "none";
            details.style.display = isHidden ? "block" : "none";
            button.textContent = isHidden ? "隐藏详情" : "显示详情";
        });
    });

    // 滑动搜索组件逻辑
    const slider = document.getElementById("date-range");
    const display = document.getElementById("date-display");
    if (slider && display) {
        slider.addEventListener("input", () => {
            display.textContent = `${slider.value} 天`;
        });
    }
});