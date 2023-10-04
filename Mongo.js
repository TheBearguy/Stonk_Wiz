To connect MongoDB to a website, you'll typically need a server-side script (e.g., using Node.js) that interacts with the MongoDB database and handles HTTP requests from your website. Below is a simplified example using Node.js and the Express.js framework to create a basic website that connects to MongoDB. Make sure you have Node.js and MongoDB installed.

1. Install required packages:

```bash
npm install express mongoose
```

2. Create an `app.js` file with the following code:

```javascript
const express = require('express');
const mongoose = require('mongoose');

const app = express();
const port = 3000;

// MongoDB connection
mongoose.connect('mongodb://localhost/yourdatabase', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define a MongoDB Schema and Model
const Schema = mongoose.Schema;
const dataSchema = new Schema({
  name: String,
  age: Number,
});

const Data = mongoose.model('Data', dataSchema);

app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.send('Welcome to your website!');
});

