function validateForm() {
  const name = document.getElementById("name").value;
  const firstName = document.getElementById("first name").value;
  const lastName = document.getElementById("last name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm-password").value;
  const termsCheckbox = document.getElementById("terms-checkbox");

  const passwordLengthRegex = /.{8,}/;
  const passwordCapitalRegex = /[A-Z]/;
  const passwordSpecialRegex = /[^A-Za-z0-9]/;

  let passwordCriteriaText = "";
  if (!passwordLengthRegex.test(password)) {
    passwordCriteriaText += "Password must be at least 8 characters long. ";
  }
  if (!passwordCapitalRegex.test(password)) {
    passwordCriteriaText += "Password must contain at least one capital letter. ";
  }
  if (!passwordSpecialRegex.test(password)) {
    passwordCriteriaText += "Password must contain a special character. ";
  }

  const passwordMatchError = document.getElementById("password-match-error");
  if (password !== confirmPassword) {
    passwordMatchError.textContent = "Passwords do not match";
    passwordMatchError.style.color = "red";
    return false;
  } else {
    passwordMatchError.textContent = "";
  }

  if (!termsCheckbox.checked) {
    alert("Please accept the Terms & Privacy Policy.");
    return false;
  }

  if (passwordCriteriaText !== "") {
    const passwordCriteria = document.createElement("p");
    passwordCriteria.classList.add("password-criteria");
    passwordCriteria.textContent = passwordCriteriaText;
    document.getElementById("confirm-password").insertAdjacentElement("afterend", passwordCriteria);
    passwordCriteria.style.color = "green";
  }

  return true;
}
