function check_input() {
  const form = document.querySelector("#form");
  form.addEventListener("submit", function () {
    if (
      document.getElementById("weight").value == "" ||
      document.getElementById("height").value == ""
    ) {
      console.log("laasd");
    }
  });
}
