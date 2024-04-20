<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Pixela Coding Graph README</h1>
    <p>This README provides an overview of the code for creating and managing a coding graph using the Pixela API.</p>

  <h2>Getting Started</h2>
  <ol>
        <li>Ensure you have Python installed on your system.</li>
        <li>Install the requests library using pip: <code>pip install requests</code>.</li>
   </ol>

  <h2>Usage</h2>
   <ol>
        <li>Replace the placeholders for <code>username</code>, <code>token</code>, and <code>graph_id</code> with your actual Pixela username, token, and desired graph ID.</li>
        <li>Uncomment the code to create a new user if you haven't done so already.</li>
        <li>Uncomment the code to create a new graph.</li>
        <li>Run the script. It will prompt you to enter the number of commits you made today.</li>
        <li>The script will then send a POST request to add the commits to your graph.</li>
        <li>Optionally, you can update or delete the commit data using the provided endpoints.</li>
    </ol>

  <h2>Endpoints</h2>
    <ul>
        <li><strong>Create User:</strong> POST request to <code>/v1/users</code></li>
        <li><strong>Create Graph:</strong> POST request to <code>/v1/users/{username}/graphs</code></li>
        <li><strong>Add Pixel:</strong> POST request to <code>/v1/users/{username}/graphs/{graph_id}</code></li>
        <li><strong>Update Pixel:</strong> PUT request to <code>/v1/users/{username}/graphs/{graph_id}/{date}</code></li>
        <li><strong>Delete Pixel:</strong> DELETE request to <code>/v1/users/{username}/graphs/{graph_id}/{date}</code></li>
    </ul>

  <h2>Dependencies</h2>
    <ul>
        <li><a href="https://docs.python-requests.org/en/latest/">Requests</a>: HTTP library for making requests in Python.</li>
    </ul>

  <h2>References</h2>
  <ul>
        <li><a href="https://pixe.la/">Pixela API Documentation</a></li>
    </ul>
</body>
</html>
