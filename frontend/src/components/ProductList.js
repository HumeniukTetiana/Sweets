import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom'; // Link додано
import '../styles/ProductList.css';

const ProductList = () => {
  const { categoryId } = useParams();
  const [products, setProducts] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('token');
    fetch(`http://localhost:8000/categories/${categoryId}/products/`, {
      headers: {
        'Authorization': `Token ${token}`,
      },
    })
      .then(res => {
        if (!res.ok) throw new Error('Unauthorized or error fetching data');
        return res.json();
      })
      .then(data => setProducts(data))
      .catch(err => {
        console.error(err);
        setError('Unable to load products. Please log in.');
      });
  }, [categoryId]);

  return (
    <div className="product-list-container">
      {error && <p className="error">{error}</p>}
      <div className="product-list">
        {products.map(product => (
          <Link
            to={`/products/${product.id}`}
            key={product.id}
            className="product-card-link"
          >
            <div className="product-card">
              <h3>{product.product_name}</h3>
              <p>Ціна: {Number(product.price).toFixed(2)} ₴</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default ProductList;
