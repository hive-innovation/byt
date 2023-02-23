var heading = document.getElementById("rollin");
  var currentText = "live";

  // Define the function to transition to the next slide
  function rollIn() {
    // Calculate the initial position of the text based on the previous slide
    var initialPosition = "translateX(0.3cm)";

    // Set the initial position of the text
    heading.style.transform = initialPosition;

    // Animate the text to roll in from the right
    heading.animate([
      { transform: initialPosition },
      { transform: "translateX(0)" }
    ], {
      duration: 1000,
      fill: "forwards"
    });

    // Update the text content to the next slide
    setTimeout(function() {
      if (currentText === "live") {
        heading.innerHTML = "learn";
        currentText = "learn";
      } else {
        heading.innerHTML = "live";
        currentText = "live";
      }
    }, 0);
  }

  // Start the animation
  setInterval(rollIn, 3000);
