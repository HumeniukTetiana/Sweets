// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/header.css';

const Header = () => (
  <header className="site-header">
    <div className="logo">🍫 Sweet Shop</div>
    <div className="header-buttons">
      <Link to="/auth/login/">Login</Link>
      <Link to="/auth/register/">Register</Link>
      <Link to="/cart/">🛒 Cart</Link>
    </div>
  </header>
);

export default Header;
