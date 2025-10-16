This is a Streamlit-powered personal portfolio web app built to showcase my experience, projects, and contact information in an elegant, interactive way.
It includes sections for About Me, Projects, and Contact, with a custom-designed UI featuring gradient animations, modern layout, and Formspree integration for sending messages directly to my email.

**Features**

✅ Dynamic Multi-Section Layout

“About Me” with a professional summary and core competencies.
“Projects” showcasing technical skills (Machine Learning, NLP, API Development).
“Contact” section with icons, links, and an integrated message form.

✅ Custom Styling

Gradient text headers and smooth animated background.
Modern UI with custom HTML + CSS inside Streamlit.

✅ Email Form (Formspree Integration)

Visitors can send messages directly via Formspree API.
Input validation with success/error messages handled inside Streamlit.

✅ Modular OOP Design

Each section (info, projects, contact) is defined in separate class methods.
Inheritance (_portfolio → stream) used for clean structure.

**🧠 Tech Stack**

-Component	Technology
-Frontend	Streamlit + HTML + CSS
-Backend	Python

**🛡️ Security**

-Formspree ensures all form data is transmitted securely over HTTPS.
-No credentials or secrets are stored in your code — your Formspree endpoint handles delivery.
-Users’ email and message content are only visible to you (the recipient)

**Future Enhancements**

✅ Add Google reCAPTCHA to prevent bot submissions
✅ Include more projects with visuals
✅ Deploy on Streamlit Cloud or Render
Email Handling	Formspree API

Design	Custom CSS gradients, columns, and layout management
