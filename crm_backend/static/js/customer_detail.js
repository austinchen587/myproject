document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("add-comment-form");
    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            fetch(form.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.message) {
                        const commentsList = document.querySelector(".comments-timeline");
                        const newComment = document.createElement("li");
                        newComment.innerHTML = `
                            <div class="comment-meta">
                                <strong>${data.comment.created_by}</strong> 于 ${data.comment.created_at}
                            </div>
                            <div class="comment-content">
                                ${data.comment.content}
                            </div>
                        `;
                        commentsList.prepend(newComment);
                        form.reset();
                    } else if (data.error) {
                        alert(data.error);
                    }
                })
                .catch((error) => console.error("添加评论失败:", error));
        });
    }
});