import React from 'react'
import { Outlet, Link } from "react-router-dom";
// import logo from './logo.png'
import './Nav.css'
export default function Nav() {
  return (
    <div>

<nav className="container-fluid navbar navbar-expand-lg bg-white fixed-top">
  <div className="container-fluid d-flex mx-xl-5">
    <span className="navbar-brand mx-xl-5 mx-2" style={{'font-family': 'Anton, san-serif','font-weight': '900','font-style': 'normal','color':'rgb(255, 108, 11)',}}>Portfolio</span>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse justify-content-center bg-white" id="navbarNavDropdown">
      <ul className="navbar-nav">
        <li className="nav-item mx-5">
        <Link className=" nav-link text-center lis py-xl-1 px-xl-2" to="/Home">Home</Link>
        </li>
        <li className="nav-item mx-5">
        <Link className=" nav-link text-center lis py-xl-1 px-xl-2" to="/Project">Project</Link>
        </li>
        <li className="nav-item mx-5">
        <Link className=" nav-link text-center lis py-xl-1 px-xl-2" to="/About">About</Link>
        </li>
        <li className="nav-item mx-5">
        <Link className=" nav-link text-center lis py-xl-1 px-xl-2" to="/Contact">Contact</Link>
        </li>
      </ul>
    </div>
  </div>
</nav>
       <div className='container-flulid mt-5'>
       <Outlet/>
       </div>
    </div>
  )
}