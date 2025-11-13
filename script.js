fetch("jobs.json")
    .then(response => response.json())
    .then(jobs => {
        const container = document.getElementById("jobs");

        jobs.forEach(job => {
            const card = document.createElement("div");
            card.className = "job-card";

            card.innerHTML = `
                <h2>${job.title}</h2>
                <p><strong>${job.company}</strong></p>
                <p><em>${job.site}</em></p>
                <a href="${job.link}" target="_blank">View Job</a>
            `;

            container.appendChild(card);
        });
    });
