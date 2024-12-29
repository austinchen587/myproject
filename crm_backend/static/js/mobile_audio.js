// 验证脚本加载
console.log("mobile_audio.js 加载成功！");

document.addEventListener("DOMContentLoaded", function () {
    console.log("脚本已加载，开始绑定事件...");

    // 文件大小验证
    const fileInput = document.getElementById("audioFileInput");
    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const file = this.files[0];
            if (file && file.size > 100 * 1024 * 1024) { // 100MB 限制
                alert("文件大小不能超过 100MB！");
                this.value = ""; // 清空文件选择框
            }
        });
    }

    // 获取录音上传表单和相关元素
    const uploadForm = document.getElementById("uploadAudioForm");
    const uploadButton = document.getElementById("uploadButton");
    const progressDiv = document.getElementById("uploadProgress");
    const audioRecordList = document.getElementById("audioRecordList");

    // 录音上传功能
    if (uploadForm) {
        uploadForm.addEventListener("submit", function (event) {
            event.preventDefault();
            console.log("上传按钮被点击，开始上传...");

            uploadButton.disabled = true; // 禁用按钮防止重复提交
            progressDiv.style.display = "block"; // 显示上传进度

            const formData = new FormData(this);
            const customerId = this.dataset.customerId;

            fetch(`/customers/recording/upload/${customerId}/`, {
                method: "POST",
                body: formData,
                headers: { "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value }
            })
                .then(response => {
                    console.log("服务器响应状态:", response.status);
                    return response.json();
                })
                .then(data => {
                    console.log("服务器返回数据:", data);
                    if (data.error) {
                        alert(data.error);
                    } else {
                        // 添加新录音到列表
                        const newItem = document.createElement("li");
                        newItem.id = `recording-${data.recording_id}`;
                        newItem.innerHTML = `
                            <p>上传时间: ${data.uploaded_at}</p>
                            <audio controls>
                                <source src="${data.file_url}" type="audio/mpeg">
                                您的浏览器不支持音频播放。
                            </audio>
                            <button class="delete-audio-btn" data-recording-id="${data.recording_id}">删除</button>
                        `;
                        audioRecordList.appendChild(newItem);

                        // 绑定删除事件
                        newItem.querySelector(".delete-audio-btn").addEventListener("click", deleteAudioHandler);

                        alert("录音上传成功！");
                    }
                })
                .catch(error => {
                    console.error("录音上传失败:", error);
                    alert("录音上传失败，请重试！");
                })
                .finally(() => {
                    uploadButton.disabled = false; // 重新启用按钮
                    progressDiv.style.display = "none"; // 隐藏上传进度
                });
        });
    }

    // 录音删除功能
    function deleteAudioHandler(event) {
        const recordingId = this.dataset.recordingId;
        if (confirm("确定要删除这条录音吗？")) {
            this.disabled = true; // 防止重复点击
            fetch(`/customers/recording/delete/${recordingId}/`, {
                method: "POST",
                headers: { "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value }
            })
                .then(response => response.json())
                .then(data => {
                    console.log("删除响应数据:", data);
                    if (data.error) {
                        alert(data.error);
                        this.disabled = false;
                    } else {
                        document.getElementById(`recording-${recordingId}`).remove(); // 删除列表项
                        alert("录音删除成功！");
                    }
                })
                .catch(error => {
                    console.error("录音删除失败:", error);
                    alert("录音删除失败，请重试！");
                    this.disabled = false;
                });
        }
    }

    // 切换详情显示
    document.querySelectorAll(".toggle-details-btn").forEach(button => {
        button.addEventListener("click", function () {
            const details = this.closest(".customer-card").querySelector(".customer-details");
            if (details) {
                const isHidden = details.style.display === "none" || details.style.display === "";
                details.style.display = isHidden ? "block" : "none";
                this.textContent = isHidden ? "隐藏更多详情" : "显示更多详情";
            }
        });
    });

    // 切换录音信息显示
    document.querySelectorAll(".toggle-audio-btn").forEach(button => {
        button.addEventListener("click", function () {
            const audioSection = this.closest(".customer-card").querySelector(".customer-audio-section");
            if (audioSection) {
                const isHidden = audioSection.style.display === "none" || audioSection.style.display === "";
                audioSection.style.display = isHidden ? "block" : "none";
                this.textContent = isHidden ? "隐藏录音信息" : "显示录音信息";
            }
        });
    });
});