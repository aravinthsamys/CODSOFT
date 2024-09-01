import React,{useEffect,useState} from "react";

export default function About() {

  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  
  const fadeInStyle = {
    opacity: isVisible ? 1 : 0,
    transition: 'opacity 1.5s ease-in-out',
  };
  return (
    <><div className={`fade-in ${isVisible ? 'visible' : ''}`} style={fadeInStyle}>
      <div className="m-3 m-xl-5">
        <h3
          className="text-center mb-4 text-warning acon"
          style={{fontWeight:'700'}}        >
          &nbsp; About &nbsp;
        </h3>
        <p className="bcon">
          I'm Aravinthsamy Sankar completing my Master of Computer Applications
          at Gnanamani College of Technology in Namakkal.  Proud to have
          studied at this esteemed institution and also at Sengunthar Arts and
          Science College in Tiruchengode, Namakkal district. Both colleges
          provided to me with a solid foundation and a supportive environment that
          encouraged him to achieve my goals. Aravinthsamy deeply respects my
          staff members for their guidance and motivation throughout my
          academic journey.</p>
          
          <h3
          className="text-center mb-4 text-info acon"
          style={{fontWeight:'700'}}        >
          &nbsp; Education &nbsp;
        </h3>
        <div className="mt-5 ed acon">
            <h6>GNANAMANI COLLEGE OF TECHNOLOGY</h6>
            <li>- Pachal,Namakkal</li>
            <li>- Master of Computer Applications (M.C.A)</li>
            <li> &nbsp; (2022 - 2024)</li>
        </div>
        <div className="my-5 ed acon">
            <h6>SENGUNTHAR ARTS AND SCIENCE COLLEGE</h6>
            <li>- Neikarapatti,Namakkal</li>
            <li>- Bachelor of Science in Computer Science( B.Sc (CS) )</li>
            <li> &nbsp; (2019 - 2022)</li>
        </div>
          
        <h3
          className="text-center mb-4 text-danger "
          style={{fontWeight:'700'}}        >
          &nbsp; Experience &nbsp;
        </h3>
           <p>During my internship at IPCS Global in Erode,
          I had a golden opportunity to learn and grow. As a Python
          trainee for three months, he gained hands-on experience and enhanced
          my technical skills. The internship was a significant milestone,
          allowing me to collaborate with colleagues, friends, and students,
          further enriching his learning experience. I am now looking
          forward to joining a leading IT company where I can continue to
          expand my knowledge and skills. i am eager to learn from industry
          experts and contribute to innovative projects. With a strong
          educational background and practical experience,then
          prepared to take on new challenges and excel in the dynamic field of
          information technology.
        </p>
      </div></div>
    </>
  );
}
