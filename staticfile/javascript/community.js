// Get the necessary elements from the DOM
const createPostButton = document.getElementById("create-post-button");
const postsContainer = document.querySelector("main");

// Listen for clicks on the Create Post button
createPostButton.addEventListener("click", () => {
  // Display a dialog box to create a new post
  const postTitle = prompt("Enter the post title:");
  const postBody = prompt("Enter the post body:");
  
  // Create a new post element and append it to the posts container
  const newPost = createPostElement(postTitle, postBody);
  postsContainer.appendChild(newPost);
});

// Listen for clicks on the Like and Downvote buttons of each post
postsContainer.addEventListener("click", (event) => {
  const target = event.target;
  
  if (target.classList.contains("like-button")) {
    // Get the previous number of likes or default to 0 if it's not set
    let likes = parseInt(target.dataset.likes) || 0;
    // Increment the number of likes and update the button text
    likes++;
    target.textContent = `Like (${likes})`;
    // Store the new number of likes in the dataset
    target.dataset.likes = likes;
  } else if (target.classList.contains("downvote-button")) {
    // Get the previous number of downvotes or default to 0 if it's not set
    let downvotes = parseInt(target.dataset.downvotes) || 0;
    // Increment the number of downvotes and update the button text
    downvotes++;
    target.textContent = `Downvote (${downvotes})`;
    // Store the new number of downvotes in the dataset
    target.dataset.downvotes = downvotes;
  } else if (target.classList.contains("comment-button")) {
    // Display a dialog box to create a new comment
    const commentBody = prompt("Enter your comment:");
    if (commentBody) {
      // Create a new comment element and append it to the post
      const newComment = createCommentElement(commentBody);
      target.closest(".post").appendChild(newComment);
    }
  }
});

// Helper function to create a new post element
function createPostElement(title, body) {
  const post = document.createElement("section");
  post.classList.add("post");
  
  const postTitle = document.createElement("h2");
  postTitle.classList.add("post-title");
  postTitle.textContent = title;
  post.appendChild(postTitle);
  
  const postMeta = document.createElement("div");
  postMeta.classList.add("post-meta");
  post.appendChild(postMeta);
  
  const postAuthor = document.createElement("span");
  postAuthor.classList.add("post-author");
  postAuthor.textContent = "Anonymous";
  postMeta.appendChild(postAuthor);
  
  const postTimestamp = document.createElement("span");
  postTimestamp.classList.add("post-timestamp");
  postTimestamp.textContent = new Date().toLocaleDateString();
  postMeta.appendChild(postTimestamp);
  
  const postBody = document.createElement("div");
  postBody.classList.add("post-body");
  postBody.textContent = body;
  post.appendChild(postBody);
  
  const postActions = document.createElement("div");
  postActions.classList.add("post-actions");
  post.appendChild(postActions);
  
  const likeButton = document.createElement("button");
  likeButton.classList.add("like-button");
  likeButton.textContent = "Like (0)";
  postActions.appendChild(likeButton);
  
  const commentButton = document.createElement("button");
  commentButton.classList.add("comment-button");
  commentButton.textContent = "Comment";
  postActions.appendChild(commentButton);
  
  const downvoteButton = document.createElement("button");
 
  downvoteButton.classList.add("downvote-button");
  downvoteButton.textContent = "Downvote (0)";
  postActions.appendChild(downvoteButton);
  
  return post;
  }
  
  // Helper function to create a new comment element
  function createCommentElement(body) {
  const comment = document.createElement("div");
  comment.classList.add("comment");
  
  const commentAuthor = document.createElement("span");
  commentAuthor.classList.add("comment-author");
  commentAuthor.textContent = "Anonymous";
  comment.appendChild(commentAuthor);
  
  const commentBody = document.createElement("div");
  commentBody.classList.add("comment-body");
  commentBody.textContent = body;
  comment.appendChild(commentBody);
  
  return comment;
  }