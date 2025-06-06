import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/forms.css';

const RegisterForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password1: '',
    password2: ''
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
      const response = await fetch('http://localhost:8000/auth/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data?.error || 'An error occurred');
      }

      if (data?.token) {
        localStorage.setItem('authToken', data.token);
        navigate('/category/'); // change the path if needed
      } else {
        throw new Error('No token received from server');
      }

    } catch (err) {
      setError('Registration error: ' + err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input
        type="text"
        name="username"
        placeholder="Username"
        onChange={handleChange}
        required
      />
      <input
        type="email"
        name="email"
        placeholder="Email"
        onChange={handleChange}
        required
      />
      <input
        type="password"
        name="password1"
        placeholder="Password"
        onChange={handleChange}
        required
      />
      <input
        type="password"
        name="password2"
        placeholder="Confirm Password"
        onChange={handleChange}
        required
      />
      <button type="submit">Register</button>
      {error && <div className="error">{error}</div>}
    </form>
  );
};

export default RegisterForm;
