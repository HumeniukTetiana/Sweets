import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import '../styles/ProductDetails.css';

const ProductDetails = () => {
  const { productId } = useParams();
  const [product, setProduct] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('token');
    fetch(`http://localhost:8000/products/${productId}/`, {
      headers: {
        'Authorization': `Token ${token}`,
      },
    })
      .then(res => {
        if (!res.ok) throw new Error('Error fetching product');
        return res.json();
      })
      .then(data => setProduct(data))
      .catch(err => {
        console.error(err);
        setError('Unable to load product.');
      });
  }, [productId]);

  const handleAddToCart = () => {
    alert(`Added "${product.product_name}" to cart!`);
  };

  const handleAddToFavorites = () => {
    alert(`Added "${product.product_name}" to favorites!`);
  };

  if (error) {
    return <div className="product-details-container"><p className="error">{error}</p></div>;
  }

  if (!product) {
    return <div className="product-details-container"><p>Loading...</p></div>;
  }

  return (
    <div className="product-details-container">
      <div className="product-card-details">
        <h2>{product.product_name}</h2>
        <p><strong>Description:</strong> {product.product_description || 'No description available.'}</p>
        <p><strong>Price:</strong> {Number(product.price).toFixed(2)} ₴</p>

        <div className="buttons-container">
          <button className="add-to-cart" onClick={handleAddToCart}>Add to Cart</button>
          <button className="add-to-favorites" onClick={handleAddToFavorites}>Add to Favorites</button>
        </div>
      </div>
      {/* You can add more content here on the right side if needed */}
    </div>
  );
};

export default ProductDetails;
