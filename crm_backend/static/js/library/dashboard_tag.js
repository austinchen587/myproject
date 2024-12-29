document.addEventListener("DOMContentLoaded", function () {
    // 查找所有复选框
    const checkboxes = document.querySelectorAll(".tag-checkbox");

    checkboxes.forEach((checkbox) => {
        // 添加点击事件监听
        checkbox.addEventListener("change", function () {
            const isChecked = this.checked;

            // 更新子标签的选中状态
            updateChildTags(this, isChecked);

            // 更新父标签的选中状态
            updateParentTags(this);
        });
    });

    // 更新子标签的状态
    function updateChildTags(checkbox, isChecked) {
        const li = checkbox.closest("li");
        const childCheckboxes = li.querySelectorAll(".child-tags .tag-checkbox");
        childCheckboxes.forEach((childCheckbox) => {
            childCheckbox.checked = isChecked;
        });
    }

    // 更新父标签的状态
    function updateParentTags(checkbox) {
        const li = checkbox.closest("li");
        const parentUl = li.parentElement.closest("li");

        if (!parentUl) return; // 如果已经是顶级标签，无需更新

        const parentCheckbox = parentUl.querySelector("> .tag-content > label > .tag-checkbox");

        // 检查同级复选框的状态
        const siblingCheckboxes = parentUl.querySelectorAll(".child-tags .tag-checkbox");
        const allChecked = Array.from(siblingCheckboxes).every((cb) => cb.checked);
        const someChecked = Array.from(siblingCheckboxes).some((cb) => cb.checked);

        parentCheckbox.checked = allChecked; // 全部选中
        parentCheckbox.indeterminate = !allChecked && someChecked; // 部分选中

        // 递归更新父级
        updateParentTags(parentCheckbox);
    }
});