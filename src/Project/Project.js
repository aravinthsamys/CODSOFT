import React,{useEffect,useState} from "react";

export default function Project() {

  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const fadeInStyle = {
    opacity: isVisible ? 1 : 0,
    transition: 'opacity 1.5s ease-in-out',
  };


  return (
    < ><div className={`fade-in ${isVisible ? 'visible' : ''}`} style={fadeInStyle}>
        
 
      <div className="mx-4 mx-xl-5 mt-3 my-4 ">
        <h3
          className="text-center mb-4 "
          style={{color:'orange',fontWeight:'700'}}
        >
          &nbsp; Projects &nbsp;
        </h3>
        <h2 className="mt-4 text-decoration-underline bcon" style={{ textUnderlineOffset: "7px",lineHeight:'1.5' }}>
          CodSoft Internship Projects as Tasks of Mini Python Programming Projects are : 
        </h2>
<br/>
<ul style={{border:'none',}}>
  <li>Simple Arithmetic Calculator</li>
  <li>Rock, Paper, Scissor Game Using Python</li>
  <li>To-Do List using MySQL with python</li>
</ul>

<p>Projects are uploaded in Github, Link in Home Page to Redirect .</p>

        <h2 className="mt-4 text-decoration-underline bcon" style={{ textUnderlineOffset: "7px",lineHeight:'1.5' }}>
          Online Based Business Promotion For Organization Or Private Sectors
          And Startup Companies
        </h2>
        <br />
        <p className="acon">
          This project aims to explore the strategic use of digital marketing
          for promoting organizations and startups in the globalized world. The
          project will Analysis the trends, challenges, and opportunities in
          digital marketing, focusing on its cost-effective, flexible, and
          global reach. Design and develop a user-friendly website with detailed
          information about the chosen pin-code area. Attract local businesses
          looking to advertise their products or services to a specific target
          audience. investigated that ecommerce and digital marketing shows
          internet marketing is way easier rather the traditional marketing. It
          decrease the marketing cost and target marketing increases. These
          websites provide information about specific geographical areas and
          corresponding postal codes. Connect with local businesses to
          understand their needs and challenges offering review and feedback
          solution to enhance the year business visibility.
          <br/> <br/>
          <a href="https://www.ijmrset.com/upload/40_Online.pdf" target="https://www.ijmrset.com/upload/40_Online.pdf" className="text-decoration-none text-primary">Click here to Redirect Project Journal.</a>

          <br/>
         Technologies Used : Python, Django Framework, HTML, CSS, JavaScript, Bootstrap.
        </p>
     <br/>
      </div>   </div>
    </>
  );
}
