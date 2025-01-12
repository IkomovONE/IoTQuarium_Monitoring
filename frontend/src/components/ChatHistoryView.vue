<template>

    <div id="title">
  
    
      <h2>Chat History
  
  
        <div id="buttons">
  
            
  
          
  
          <button @click="goBack">Back to chat</button>

          <button @click="goBackHome">Back to home</button>
  
  
        </div>
  
      </h2>
  
    </div>
  
  
    <div class="grid-container" ref="chatContainer">
  
  
      <MessageWidget   v-for="message in messages" :id=message.role :key="message.id" :data="message"  />  
  
      <div></div>
      <div></div>
  
  
  
  
    </div>
  
  
  
    
  
    
  
  
   
    
      
  
    
  
  
  
  
      
  </template>
    
    <script>
    import axios from 'axios';
    import MessageWidget from './MessageWidget.vue';
    
    
    export default {
      name: 'DashBoard',
      components: {
        MessageWidget
      },
  
      methods: {
        goBack() {
          this.$router.back(); // Navigate back to the Dashboard
        },
        goBackHome() {
          this.$router.push('/'); // Navigate back to the Dashboard
        },
        
        autoResize(event) {
          const textarea = event.target;
          textarea.style.height = "auto"; // Reset height
          textarea.style.height = textarea.scrollHeight + "px"; // Adjust height dynamically
        },
        scrollToBottom() {
          const chatContainer = this.$refs.chatContainer;  // Get the chat container using ref
  
          // Ensure it's scrollable and scroll to the bottom
          if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;  // Scroll to the bottom
          }
        }
      },
    
     
    
      data() {
          return {
            
            messages: [
              
              { id: 1, type: "assistant", title: "Messages", description: "Loading..." },
              { id: 2, type: "user", title: "user", description: "Loading..." },
             
              
            
      
      
      
      
              ],
            message: "",
          };
        },
    
        async mounted() {
  
          this.scrollToBottom();
    
         
          try {
  
            
            const response = await axios.get('http://iotquarium.info:3000/message-history');
            const response_data = response.data;
            console.log(response_data);
  
            
    
    
            this.messages = response_data.slice(1);
  
  
            this.$nextTick(() => this.scrollToBottom());
    
    
    
    
          } catch (error) {
            console.error('Error fetching sensor data:', error);
    
            this.messages= [
              
            { role: "system", content: "No response from server / Server error, make sure it is online" },
            
    
    
            ] 
          }
        },
  
        watch: {
          widgets() {
            this.$nextTick(() => {
              this.scrollToBottom(); // Scroll to bottom when messages update
            });
          },
        },
    };
    </script>
    
    <!-- Add "scoped" attribute to limit CSS to this component only -->
    <style scoped>
      h3 {
        margin: 40px 0 0;
      }
  
  
      body {
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        height: 100vh; /* Full viewport height */
        margin: 0; /* Remove default margin */
      }
      
      
      
    
      h2 {
    
        position: relative;
    
        bottom: 0.5cm;
    
        left: 0.5cm;
    
        text-align: start;
    
        font-weight: 100;
  
        margin-bottom: 0cm;
  
        
    
    
      }
  
      #title {
  
        height: 1.2cm;
  
  
      }
  
      #buttons {
  
        box-shadow: none;
  
        background: none;
  
        width: fit-content;
  
        height: fit-content;
  
  
  
  
        position: relative;
  
        left: 5cm;
  
        bottom: 0.9cm;
  
        
  
  
  
        }
  
  
      .message-input {
  
        
        display: flex;
        align-items: center;
        padding: 1px;
        position: sticky;
        
        gap: 10px;
  
        margin-left: 4cm;
  
        margin-right: 4cm;
  
        border-radius: 20px;
        
  
        background-color: #131212c4;
  
        margin-top: 0cm;
        
  
        box-shadow:  -1px -1px 50px #000000;
  
        bottom: 0;
  
        
  
        
  
        z-index: 10;
        
        }
  
      .message-textarea {
        flex: 1;
        resize: none;
        
  
        overflow-y: auto;
        border: none;
        border-radius: 20px;
        padding: 10px 15px;
        height: 1cm;
  
        max-height: 4cm;
        margin-left: 1cm;
        
        margin-bottom: 0.3cm;
        margin-top: 0.5cm;
        margin-right: 10px;
        background: #131212c4;
        color: #e6e6e6;
  
        
        
        font-size: 14px;
        outline: none;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
      }
  
      .send-button {
  
        bottom: 0.07cm;
  
        
  
        margin-right: 1cm
  
  
      }
  
  
  
      button {
  
        position: relative;
  
        text-align: center;
  
  
  
  
        font-weight: lighter;
  
        font-size: large;
  
        margin-right: 0.5cm;
  
  
  
        border-width: 0cm;
  
  
        background: linear-gradient(145deg, #14cbc894, #3f4aee);
        color: #ffffff;
        box-shadow: 10px 10px 10px #00000032, -1px -1px 10px #05060d3f;
        border-radius: 20px;
        padding: 11px;
        
        transition: transform 0.2s ease-in-out;
  
        height: 1cm;
  
        width: fit-content;
  
  
        }
  
  
      body[data-theme="dark"] button {
        background: linear-gradient(195deg, #20202caf, #262a5c);
        
        color:  #fdfeff;
        box-shadow: 7px 7px 15px #080919, -7px -7px 15px #080919;
        
        
        transition: transform 0.2s ease-in-out;
  
        
      }
  
      button:hover {
        transform: scale(1.03);
      }
  
  
  
    
    
    
      .grid-container {
        display: flex;
         /* Flexible layout */
        row-gap: 20px;
        overflow-y: auto;
        flex-direction: column;
        min-height: 30%;
  
        
  
        max-height: 65vh;
        
        
         /* Centers the container */
        margin: 0 auto;
        
      }
    
    
     
    
      #user {
  
        align-self: flex-end;
    
        height: 3cm;
    
        width: 7.25cm;
  
        word-wrap: break-word;
  
        max-width: 60%;
  
        padding: 10px;
  
        margin-right: 2cm;
  
        height: fit-content;
    
        min-width: 5cm;
        
        width: fit-content;
  
        
  
        max-width: 40%;
  
    
    
      }
    
    
      #assistant {
    
      height: 3cm;
    
      width: 7.25cm;
  
      margin-left: 0.5cm;
  
      height: fit-content;
    
      width: fit-content;
  
      max-width: 40%;
  
      }
    
      #system {
    
      height: fit-content;
  
      max-height: 3cm;
    
      width: fit-content;
  
      max-width: 40%;
  
      margin-left: 10cm;
  
      opacity: 40%;
  
  
    
    
      }
    
    
      
    
    
      @media (max-width: 768px) {


        #buttons {

          left: 0cm;

          margin-top: 1cm;

        }

        h2 {

          font-size: 0.001cm;

        }





        .grid-container {
          display: flex;

          position: relative;

          margin-left: 0cm;

          right: 0cm;

          overflow-x: hidden;
          /* Flexible layout */
          row-gap: 2px;
          flex-direction: column;
          min-height: 10vh;
          max-width: 100vh;
          column-gap: 0px; /* Reduced column gap */
          margin-bottom: auto; /* Centers the container */
        }


        #user {

        align-self: flex-end;

        height: 3cm;

        width: 4cm;

        word-wrap: break-word;

        max-width: 60%;

        padding: 10px;

        margin-right: 1cm;



        }

          #assistant {

            align-self: unset;

            right: 0.09cm;

            margin-left: 0cm;

            align-self: start;

            position: relative;

            

            

            word-wrap: break-word;

            max-width: 40%;

            margin-bottom: 2cm;

            

          



            }



          #system {

            position: relative;

            max-height: fit-content;

            width: 7.25cm;

            word-wrap: break-word;

            max-width: 60%;

            padding: 10px;

            align-self:start;

            



          }
    
    
        
    
      }
    
      @media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {
    
       
    
       
    
        .grid-container {
    
          
    
          grid-template-columns: repeat(auto-fill, minmax(250px, 9cm));
    
          margin-bottom: 2cm
    
    
        }
    
        body {
    
          max-width: 100%;
    
          overflow-x: hidden;
    
    
        }
    
      
    
      }
    
      @media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {
    
    
       
    
        .grid-container {
  
        
  
          grid-template-columns: repeat(auto-fill, minmax(250px, 9cm));
  
        
  
        }
    
      
    
          
      }
    
    
    </style>
    