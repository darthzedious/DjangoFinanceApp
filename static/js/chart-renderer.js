function renderRepaymentChart(planId, repaymentData) {
    const periods = repaymentData.map(row => row.n);
    const remaining = repaymentData.map(row => row.RP);
    const ctx = document.getElementById(`chart-${planId}`).getContext('2d');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: periods,
            datasets: [{
                label: 'Remaining Principal',
                data: remaining,
                borderWidth: 2,
                tension: 0.2,
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: "Period" } },
                y: { beginAtZero: false }
            }
        }
    });
}
