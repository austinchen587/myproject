document.addEventListener("DOMContentLoaded", function () {
    const uploadImageForm = document.getElementById('uploadImageForm');

    if (!uploadImageForm) {
        console.error("上传图片表单未找到！");
        return;
    }

    const customerId = uploadImageForm.dataset.customerId;

    uploadImageForm.addEventListener('submit', function (e) {
        e.preventDefault(); // 阻止默认表单提交
        console.log('上传按钮被点击，开始上传...');

        const formData = new FormData(uploadImageForm);

        console.log('表单数据:', formData);
        console.log('客户 ID:', customerId);

        fetch(`/upload_image/${customerId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: formData,
        })
            .then((response) => {
                console.log('服务器响应状态码:', response.status);
                return response.json();
            })
            .then((data) => {
                console.log('服务器返回数据:', data);
                if (data.message) {
                    alert('图片上传成功！');
                    location.reload();
                } else {
                    alert(data.error || '上传失败');
                }
            })
            .catch((error) => {
                console.error('上传失败:', error);
                alert('图片上传失败，请稍后再试！');
            });
    });
});