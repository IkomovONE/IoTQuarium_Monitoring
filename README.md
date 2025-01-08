

# 🐠 Smart Aquarium Monitoring System 

Implementation of my pet project, IoT system which is expected to collect, store and send aquarium environment data to OpenAI API for GPT model analysis, and suggest maintenance actions to the user based on the provided evaluation. The idea is inspired by my passion for aquariums and by me wanting to improve the experience of aquarium keeping.

---

## Features of the system

- **Real-time continuous data collection**: The system I designed collects real-time data from my aquarium, including water temperature, pH value, Total Dissolved Solids (TDS), lamp status, water level and water flow.

- **Daily averages**: The system calculates and records daily averages of some of the above mentioned values, it's possible to access it through the database or on the dashboard view (only the latest calculation).

- **Tailored overall evaluation**: The dashboard view features overall evaluation widget which is tailored for the latest environment conditions, powered by OpenAI.

- **Ask GPT**: Feature powered by OpenAI, function allowing user to chat with GPT to ask about current conditions in the aquarium or other questions related to aquatic life.

- **Accessible from mobile devices**: The frontend application is optimized for mobile devices.


## Frontend website application
Frontend website serves as an application used to access the smart system, it features dashboard with general recent data view and askGPT function which allows to chat with OpenAI's GPT to ask questions about current aquarium conditions and other aquatic hobby related stuff. 

### Screenshots

#### Dashboard & Chat (Light Mode)
<div align="center">
  <img src="assets/dashboard_light.png" alt="Dashboard view" width="48%" />
  <img src="assets/chat_light.png" alt="Chat view" width="48%" />
</div>

### Dashboard & Chat (Dark Mode)
<div align="center">
  <img src="assets/dashboard_dark.png" alt="Dashboard Dark Mode" width="48%" />
  <img src="assets/chat_dark.png" alt="Chat Dark Mode" width="48%" />
</div>




### Technical specifics

- The frontend application is built with Vue.js

- The font used can be found here: https://fonts.google.com/specimen/Roboto+Flex

- The icons and animated logo used can be accessed here: https://www.flaticon.com

### How to run

To launch the frontend app, you need to install Node.js and Vue.js in your terminal (you can run "npm install"). In order to run the app you can use "npm run serve". In order for the app to show anything the server needs to be running too, otherwise the app will show server error widget.





## Contact

Feel free to contact me if you have any questions. My e-mail is daniil_komov@icloud.com
