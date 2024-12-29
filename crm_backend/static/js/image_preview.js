document.addEventListener("DOMContentLoaded", function () {
    console.log("image_preview.js 加载成功！");

    // 小图片预览功能
    function previewImage(event) {
        const previewImg = document.getElementById("previewImg");
        previewImg.style.display = "block";
        previewImg.src = URL.createObjectURL(event.target.files[0]);
    }

    // 绑定小图片点击事件，显示模态框
    document.querySelectorAll(".small-image").forEach(image => {
        image.addEventListener("click", function () {
            const modal = document.getElementById("imageModal");
            const fullImage = document.getElementById("fullImage");
            modal.style.display = "block";
            fullImage.src = this.dataset.fullSrc;
        });
    });

    // 关闭模态框
    const modal = document.getElementById("imageModal");
    if (modal) {
        const closeBtn = modal.querySelector(".close");
        closeBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }

    // 上传图片表单提交逻辑
    const uploadImageForm = document.getElementById("uploadImageForm");
    if (uploadImageForm) {
        uploadImageForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const customerId = this.dataset.customerId;
            const formData = new FormData(this);

            fetch(`/upload_image/${customerId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
                },
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        alert("图片上传成功！");
                        location.reload();
                    } else {
                        alert(data.error || "上传失败");
                    }
                })
                .catch(error => {
                    console.error("上传失败:", error);
                    alert("图片上传失败，请稍后再试！");
                });
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    console.log("image_preview.js 加载成功！");

    // 绑定小图片点击事件，显示模态框
    document.querySelectorAll(".small-image").forEach(image => {
        console.log("绑定事件的图片:", image.src);
        image.addEventListener("click", function () {
            const modal = document.getElementById("imageModal");
            const fullImage = document.getElementById("fullImage");
            modal.style.display = "block";
            fullImage.src = this.dataset.fullSrc;
        });
    });

    // 关闭模态框
    const modal = document.getElementById("imageModal");
    if (modal) {
        const closeBtn = modal.querySelector(".close");
        closeBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    console.log("image_preview.js 加载成功！");

    document.querySelectorAll(".small-image").forEach(image => {
        console.log("绑定事件的图片:", image.src); // 输出图片的 URL
        image.addEventListener("click", function () {
            const modal = document.getElementById("imageModal");
            const fullImage = document.getElementById("fullImage");
            modal.style.display = "block";
            fullImage.src = this.dataset.fullSrc;
        });
    });
});