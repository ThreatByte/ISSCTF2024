const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();

// Secret key used to sign and verify JWT tokens
const secretKey = '0830328284'

// Middleware to verify JWT token
function authenticateToken(req, res, next) {
  const token = req.headers['authorization'];

  if (!token) {
    return res.status(401).json({ message: 'Authentication token missing' });
  }

  jwt.verify(token, secretKey, (err, user) => {
    if (err) {
      return res.status(403).json({ message: 'Invalid token' });
    }

    req.user = user;
    next();
  });
}

// API endpoint that requires authentication
app.get('/api/secret', authenticateToken, (req, res) => {
  const userRole = req.user.role;
  let message = '';

  if (userRole === 'admin') {
    message = 'EspionageCTF{stealing_tokens_is_bad}';
  } else if (userRole === 'user') {
    message = 'Nice try!';
  }
  res.json({ message });
});
// Generate JWT token
app.get('/api/token', (req, res) => {
  const payload = { username: 'admin', role: 'user' };
  const token = jwt.sign(payload, secretKey);
  res.json({ token });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});



/*
const CryptoJS = require('crypto-js');

const encryptWithAES = (text) => {
  const passphrase = '123';
  return CryptoJS.AES.encrypt(text, passphrase).toString();
};

const decryptWithAES = (ciphertext) => {
  const passphrase = '123';
  const bytes = CryptoJS.AES.decrypt(ciphertext, passphrase);
  const originalText = bytes.toString(CryptoJS.enc.Utf8);
  return originalText;
};
*/
