import React from 'react';

const Cart = () => {
  // Поки немає логіки — просто відображаємо, що кошик порожній
  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h2>🛒 Ваш кошик</h2>
      <p>Кошик порожній.</p>
    </div>
  );
};

export default Cart;
