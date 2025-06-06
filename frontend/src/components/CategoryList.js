import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/CategoryList.css';

// Імпорт локальних зображень
import cakepops from '../images/cakepops.jpg';
import cakes from '../images/cakes.jpg';
import cookies from '../images/cookies.jpg';
import cupcakes from '../images/cupcakes.jpg';

const imageMap = {
  cakepops,
  cakes,
  cookies,
  cupcakes
};

const CategoryList = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/categories/')
      .then(res => res.json())
      .then(data => setCategories(data))
      .catch(err => console.error("Error fetching categories:", err));
  }, []);

  const getImage = (categoryName) => {
    const key = categoryName?.toLowerCase().trim();
    return imageMap[key] || 'https://via.placeholder.com/220x140?text=No+Image';
  };

  return (
    <>
      <div className="hero-section">
        <h1>Welcome!</h1>
        <p>Pick something to your taste</p>
      </div>

      <div className="category-container">
        <div className="category-grid">
          {categories.map((category, index) => {
            const name = category.category_name || category.name || 'Untitled';
            const backgroundImage = `url(${getImage(name)})`;

            return (
              <Link
                to={`/categories/${category.id}/products`}
                key={category.id}
                className="category-card"
                style={{
                  animationDelay: `${index * 0.1}s`,
                  '--bg-img': backgroundImage
                }}
              >
                <span>{name}</span>
              </Link>
            );
          })}
        </div>
      </div>
    </>
  );
};

export default CategoryList;
