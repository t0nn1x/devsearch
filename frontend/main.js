let projectsUrl = "http://127.0.0.1:8000/api/projects/"

let getProjects = () => {
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
}

getProjects()

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById("projects-wrapper")

    for(let i = 0; i < projects.length; i++) {
        let project = projects[i]
        let projectDiv = document.createElement("div")
        projectDiv.className = "project--card"
        projectDiv.innerHTML = `
            <img src="http://127.0.0.1:8000${project.featured_image}">
            <div>
                <div class="card--header">
                    <h3>${project.title}</h3>
                    <strong class="vote--option">&#43;</strong>
                    <strong class="vote--option">&#8722;</strong>
                </div>
                <i>${project.vote_ratio}% Positive Feedback</i>
                <p>${project.description.substring(0, 150)}</p>
            </div>
        `
        projectsWrapper.appendChild(projectDiv)
    }
}