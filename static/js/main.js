let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();

      let page = this.dataset.page;
      console.log("Page: ", page);

      searchForm.innerHTML += `<input type="hidden" name="page" value="${page}">`;
      searchForm.submit();
    });
  }
}
