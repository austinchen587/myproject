let radarChart;

function updateData() {
    const userSelect = document.getElementById("user-select");
    const groupSelect = document.getElementById("group-select");
    const batchSelect = document.getElementById("batch-select");

    const userId = userSelect ? userSelect.value : "";
    const groupId = groupSelect ? groupSelect.value : "";
    const batchNumber = batchSelect ? batchSelect.value : "";

    fetch(`/get_completion_data/?user_id=${userId}&group_id=${groupId}&batch_number=${batchNumber}`)
        .then(response => response.json())
        .then(data => {
            const labels = Object.keys(data.completion_rates);
            const completionRates = Object.values(data.completion_rates);

            if (radarChart) {
                radarChart.destroy();
            }

            const ctx = document.getElementById("completionRadarChart").getContext("2d");
            radarChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: '完成度 (%)',
                        data: completionRates,
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scale: {
                        ticks: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            });
        });

    fetch(`/data_analysis_json/?selected_user=${userId}&selected_group=${groupId}&batch_number=${batchNumber}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("data-rows");
            tableBody.innerHTML = "";

            let totals = { contacted: 0, invited: 0, wechat: 0, joined: 0, closed: 0, overall: 0 };
            data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${row.student_batch}</td>
                    <td>${row.contacted_count}</td>
                    <td>${row.invited_count}</td>
                    <td>${row.wechat_added_count}</td>
                    <td>${row.joined_count}</td>
                    <td>${row.closed_count}</td>
                    <td>${row.total_count}</td>
                `;
                tableBody.appendChild(tr);

                totals.contacted += row.contacted_count;
                totals.invited += row.invited_count;
                totals.wechat += row.wechat_added_count;
                totals.joined += row.joined_count;
                totals.closed += row.closed_count;
                totals.overall += row.total_count;
            });

            document.getElementById("total-contacted").textContent = totals.contacted;
            document.getElementById("total-invited").textContent = totals.invited;
            document.getElementById("total-wechat").textContent = totals.wechat;
            document.getElementById("total-joined").textContent = totals.joined;
            document.getElementById("total-closed").textContent = totals.closed;
            document.getElementById("overall-total").textContent = totals.overall;
        });
}

document.addEventListener("DOMContentLoaded", updateData);