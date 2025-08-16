$(document).on("click", "#signup_submit", function () {
  let data = {
    username: $(".username").val(),
    email: $(".email").val(),
    password: $(".password").val(),
  };

  $.ajax({
    type: "POST", // must be POST
    url: "/world/signup/validate/", // include world/ if using that prefix
    contentType: "application/json", // send as JSON
    data: JSON.stringify(data), // stringify the object
    success: function (result) {
      if (result.success) {
        window.location.href = "/world/login/"; // adjust URL
      } else {
        alert(result.message);
      }
    },
    error: function () {
      alert("Signup failed. Please try again.");
    },
  });
});
