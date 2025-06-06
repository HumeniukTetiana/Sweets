// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CategoryList from './components/CategoryList';
import ProductDetails from './components/ProductDetails';
import Header from './components/Header';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/LoginForm';
import Cart from './components/Cart';
import ProductListByCategory from './components/CategoryList';
import ProductList from './components/ProductList';



function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<CategoryList />} />
        <Route path="/products/:productId" element={<ProductDetails />} />
        <Route path="/auth/register" element={<RegisterForm />} />
        <Route path="/auth/login" element={<LoginForm />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/category/" element={<CategoryList />} />
        <Route path="/categories/:categoryId/products" element={<ProductList />} />
      </Routes>
    </Router>
  );
}

export default App;
