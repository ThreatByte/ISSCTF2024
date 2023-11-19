const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3721;

app.use(cors());
app.use(bodyParser.json());

const checkApiKey = (req, res, next) => {
  const apiKey = req.body.apiKey;

  if(apiKey == null || apiKey == undefined) {
    return res.status(200).json({ error: 'No API key' });
  }

  if (!apiKey.includes('test_') && !apiKey.includes('prod_')) {
    return res.status(200).json({ error: 'Invalid API key' });
  }

  next();
};

app.post('/ping', checkApiKey, (req, res) => {
  res.json({ message: 'Pong, API is online!' });
});

app.post('/getNodes', checkApiKey, (req, res) => {
  const apiKey = req.body.apiKey;
  res.json({ message: 'https://files.catbox.moe/3xayl1.webm', apiKey });
});

app.post('/getImportant', checkApiKey, (req, res) => {
  const apiKey = req.body.apiKey;
  res.json({ message: 'https://www.youtube.com/embed/0Jx8Eay5fWQ', apiKey });
});

function doesNotExist(variable) {
  return variable == undefined || variable == null || variable == ''
}

app.post('/internal', checkApiKey, (req, res) => {
  const apiKey = req.body.apiKey;
  const password = req.body.password;

  if(apiKey != 'test_30da4632313e8404c8bdee6917079f96') {
    res.json({ error: 'Authorized users only.' })
    return
  }

  if(doesNotExist(password)) {
    res.json({ error: 'Parameter "password" is missing.' })
    return
  }

  if(password == 'god') {
    res.json({ flag: 'EspionageCTF{MessW1thTh3BestD1eL1keTh3Rest}' })
    return
  }
  else {
    res.json({ error: 'Incorrect password for systems operator. https://www.youtube.com/embed/9Q8jQr81Nyc' })
    return
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});