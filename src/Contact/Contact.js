import React,{useEffect,useState} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import emailjs from 'emailjs-com';

export default function Contact(){

  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);
  
  const fadeInStyle = {
    opacity: isVisible ? 1 : 0,
    transition: 'opacity 1.5s ease-in-out',
  };

function sendEmail(e){
  e.preventDefault();
  emailjs.sendForm('service_captcha486','template_63gcx34',e.target,'bT_RHPQwrhnpDem2E')
  .then((result)=>{
    window.location.reload()
  },(error)=>{
    console.log(error.text);
  })
}




  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };


  return (
    <div className={`fade-in ${isVisible ? 'visible' : ''}`} style={fadeInStyle}>
    <div className="m-xl-5 m-4 mt-5 w-xl-50 p-xl-5">
      <h2 className='text-info text-center acon' style={{fontWeight:'700'}}>CONTACT ME </h2>
      <form onSubmit={sendEmail} className='m-xl-5 mt-5 ccon' style={{borderRadius:'10px'}}>
        <div className="mb-3 ">
          <label htmlFor="name" className="form-label " style={{fontWeight:'700'}}>Name</label>
          <input
            type="text"
            className="form-control "
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label " style={{fontWeight:'700'}}>Email</label>
          <input
            type="email"
            className="form-control "
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="subject" className="form-label " style={{fontWeight:'700'}}>Subject</label>
          <input
            type="text"
            className="form-control "
            id="subject"
            name="subject"
            value={formData.subject}
            onChange={handleChange}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="message" className="form-label " style={{fontWeight:'700'}}>Message</label>
          <textarea
            className="form-control "
            id="message"
            name="message"
            rows="4"
            value={formData.message}
            onChange={handleChange}
            required
          ></textarea>
        </div>
        <button type="button" className="btn btn-primary bcon">Send</button> <br/><br/>
        <p style={{color:'red'}}>* sample site</p>
      </form>
    </div> </div>
  );
};


