document.addEventListener("DOMContentLoaded", () => {
    // 工具函数：切换元素显示/隐藏
    const toggleVisibility = (element) => {
        const isHidden = element.style.display === "none" || element.style.display === "";
        element.style.display = isHidden ? "block" : "none";
    };

    // 切换客户详情显示/隐藏
    document.querySelectorAll(".toggle-details").forEach(button => {
        button.addEventListener("click", () => {
            const details = button.previousElementSibling; // 获取紧邻的客户详情元素
            if (details) {
                toggleVisibility(details);
                button.textContent = details.style.display === "block" ? "隐藏详情" : "显示详情";
            }
        });
    });

    // 滑动搜索组件逻辑
    const slider = document.getElementById("date-range");
    const display = document.getElementById("date-display");
    if (slider && display) {
        slider.addEventListener("input", () => {
            display.textContent = `最近 ${slider.value} 天`;
        });
        // 初始化显示值
        display.textContent = `最近 ${slider.value} 天`;
    }

    // 动态调整主容器 margin-top 防止 header 遮挡
    const header = document.querySelector('.header');
    const container = document.querySelector('.container');
    if (header && container) {
        const headerHeight = header.offsetHeight;
        container.style.marginTop = `${headerHeight}px`; // 设置 margin-top
    }

    // 添加评论按钮逻辑
    document.querySelectorAll(".add-comment-btn").forEach(button => {
        button.addEventListener("click", () => {
            const formContainer = button.nextElementSibling; // 评论表单容器
            if (formContainer) toggleVisibility(formContainer);
        });
    });

    // 提交评论逻辑
    document.querySelectorAll(".submit-comment-btn").forEach(button => {
        button.addEventListener("click", () => {
            const customerId = button.getAttribute("data-customer-id");
            const commentContent = button.previousElementSibling?.value.trim();

            if (!commentContent) {
                alert("评论内容不能为空！");
                return;
            }

            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
            if (!csrfToken) {
                alert("CSRF令牌缺失，请刷新页面后重试！");
                return;
            }

            fetch("/add_comment_ajax/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({ customer_id: customerId, content: commentContent }),
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // 在评论列表中添加新评论
                        const commentsList = button.closest(".customer-card").querySelector(".comments-timeline");
                        if (commentsList) {
                            const newComment = document.createElement("li");
                            newComment.innerHTML = `
                                <p>${data.comment.content}</p>
                                <small>由 ${data.comment.created_by} 于 ${data.comment.created_at}</small>
                            `;
                            commentsList.prepend(newComment); // 添加到评论列表顶部
                        }
                        // 清空评论输入框并隐藏表单
                        button.previousElementSibling.value = "";
                        button.closest(".add-comment-form-container").style.display = "none";
                    } else {
                        alert(data.error || "添加评论失败");
                    }
                })
                .catch(error => {
                    console.error("添加评论失败:", error);
                    alert("添加评论时出现问题，请稍后再试！");
                });
        });
    });
});


document.addEventListener("DOMContentLoaded", () => {
    const filterToggleButton = document.getElementById("toggle-filter");
    const filterForm = document.getElementById("filter-form");

    if (filterToggleButton && filterForm) {
        filterToggleButton.addEventListener("click", () => {
            const isHidden = filterForm.style.display === "none" || filterForm.style.display === "";
            filterForm.style.display = isHidden ? "block" : "none"; // 切换显示/隐藏
            filterToggleButton.textContent = isHidden ? "隐藏筛选条件" : "显示筛选条件"; // 更新按钮文字
        });
    }
});