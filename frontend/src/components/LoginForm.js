import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/forms.css';

const LoginForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });

  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await fetch('http://localhost:8000/auth/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data?.error || 'Invalid login credentials');
      }

      if (data?.token) {
        localStorage.setItem('authToken', data.token);
        navigate('/category/'); // or any route you want after login
      } else {
        throw new Error('Token was not provided by the server');
      }

    } catch (err) {
      setError('Login error: ' + err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input
        type="text"
        name="username"
        placeholder="Username"
        onChange={handleChange}
        required
      />
      <input
        type="password"
        name="password"
        placeholder="Password"
        onChange={handleChange}
        required
      />
      <button type="submit">Log In</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
};

export default LoginForm;
