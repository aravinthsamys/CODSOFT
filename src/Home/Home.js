import React,{useEffect,useState} from "react";
import robotImage from "./robot.png";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "./home.css";
export default function Home() {

  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);
  
  const fadeInStyle = {
    opacity: isVisible ? 1 : 0,
    transition: 'opacity 1.5s ease-in-out',
  };
  return (
    <div className={`fade-in ${isVisible ? 'visible' : ''} container-fluid row` } style={fadeInStyle}>
      <div className="col-xl-8 px-xl-5 py-1 con1">
        <div className="my-xl-5 py-xl-5 ">
          <h1 className="font1 mx-3 text-center">Hi, Myself ..</h1>
          <h2 className="fontofh2 text-center">Mr. Aravinthsamy Sankar</h2>
          <p className="mt-xl-5 mx-3 text-center font2">
            Lorem ipsum dolor sit amet consectetur <br/> <span style={{fontWeight:'700',color:'green'}}>CODSOFT- REACTJS DEVELOPER</span> <br/> elit. Labore ex a
            minima excepturi? Labore hic ducimus ad amet voluptate similique.
          </p>

          <div className=" d-xl-flex d-none justify-content-evenly mt-xl-5" id="mobi">
        <a href="https://github.com/aravinthsamys" target="_blank" rel="noopener noreferrer" className="btn btn-dark m-2">
          <i className="fab fa-github"></i>
        </a>
        <a href="https://in.linkedin.com/in/aravinthsamysankar" target="_blank" rel="noopener noreferrer" className="btn btn-primary m-2">
          <i className="fab fa-linkedin"></i>
        </a>
        <a href="https://www.instagram.com/aravinth6_11" target="_blank" rel="noopener noreferrer" className="btn btn-danger m-2">
          <i className="fab fa-instagram"></i>
        </a>
      </div>

        </div>
      </div>
      <div className="col-xl-4 con2">
         <div className="mt-xl-4">
             <img className="mx-5 mx-xl-0 phot" src={robotImage}  alt=""/>

             <div className="d-flex justify-content-evenly mb-3 ids my-4">
        <a href="https://github.com/aravinthsamys" target="_blank" rel="noopener noreferrer" className="btn btn-dark m-2">
          <i className="fab fa-github"></i>
        </a>
        <a href="https://in.linkedin.com/in/aravinthsamysankar" target="_blank" rel="noopener noreferrer" className="btn btn-primary m-2">
          <i className="fab fa-linkedin"></i>
        </a>
        <a href="https://www.instagram.com/aravinth6_11" target="_blank" rel="noopener noreferrer" className="btn btn-danger m-2">
          <i className="fab fa-instagram"></i>
        </a>
      </div>

         </div>


      </div>
    </div>
  );
}
