let loginBtn = document.getElementById("login-btn");
let logoutBtn = document.getElementById("logout-btn");
let token = localStorage.getItem("token");

if (token) {
  loginBtn.style.display = "none";
  logoutBtn.style.display = "block";
} else {
  loginBtn.style.display = "block";
  logoutBtn.style.display = "none";
}

logoutBtn.addEventListener("click", (e) => {
  e.preventDefault();
  localStorage.removeItem("token");
  window.location.href = "login.html";
});


let projectsUrl = "http://127.0.0.1:8000/api/projects/";

let getProjects = () => {
  fetch(projectsUrl)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      buildProjects(data);
    });
};

let buildProjects = (projects) => {
  let projectsWrapper = document.getElementById("projects-wrapper");
  projectsWrapper. innerHTML = "";

  for (let i = 0; i < projects.length; i++) {
    let project = projects[i];
    let projectDiv = document.createElement("div");
    projectDiv.className = "project--card";
    projectDiv.innerHTML = `
            <img src="http://127.0.0.1:8000${project.featured_image}">
            <div>
                <div class="card--header">
                    <h3>${project.title}</h3>
                    <strong class="vote--option" data-vote="up" data-project="${
                      project.id
                    }">&#43;</strong>
                    <strong class="vote--option" data-vote="down" data-project="${
                      project.id
                    }">&#8722;</strong>
                </div>
                <i>${project.vote_ratio}% Positive Feedback</i>
                <p>${project.description.substring(0, 150)}</p>
            </div>
        `;
    projectsWrapper.appendChild(projectDiv);
  }
  addVoteEvents();
};

let addVoteEvents = () => {
  let voteBtns = document.getElementsByClassName("vote--option");

  for (let i = 0; i < voteBtns.length; i++) {
    voteBtns[i].addEventListener("click", (e) => {
      let token = localStorage.getItem("token");
      console.log("Token", token);
        
      let vote = e.target.dataset.vote;
      let project = e.target.dataset.project;

      fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ value: vote }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Success:", data);
          getProjects();
        });
    });
  }
};

getProjects();
