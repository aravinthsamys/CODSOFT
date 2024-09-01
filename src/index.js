import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Router from './nav/Router';

// function Index() {
//   return (
//     <>
//     <Nav/>
//     </>
//   )
// }


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>
);
