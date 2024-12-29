document.addEventListener("DOMContentLoaded", function () {
    // 获取所有的复选框
    const checkboxes = document.querySelectorAll(".tag-checkbox");

    checkboxes.forEach((checkbox) => {
        // 当复选框被点击时
        checkbox.addEventListener("change", function () {
            const isChecked = this.checked;
            const level = parseInt(this.dataset.level);

            // 如果是选择了四级标签，递归选择上级标签
            if (isChecked && level === 3) {
                let parentId = this.dataset.parentId;
                while (parentId) {
                    const parentCheckbox = document.querySelector(
                        `.tag-checkbox[value="${parentId}"]`
                    );
                    if (parentCheckbox) {
                        parentCheckbox.checked = true;
                        parentId = parentCheckbox.dataset.parentId; // 获取上级标签 ID
                    } else {
                        parentId = null;
                    }
                }
            }

            // 如果取消了四级标签，自动取消下级标签（如果有的话）
            if (!isChecked) {
                const childTags = document.querySelectorAll(
                    `.tag-checkbox[data-parent-id="${this.value}"]`
                );
                childTags.forEach((child) => (child.checked = false));
            }
        });
    });
});