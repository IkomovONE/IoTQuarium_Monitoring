<template>

  

  <div id="title">

  
    <h2>Chat with AI


      <div id="buttons">

          

        <button @click="goBack">Back to home</button>

        <button @click="goToChatHistory">View chat history</button>


      </div>

    </h2>

  </div>


  <div class="grid-container" ref="chatContainer">


    <MessageWidget   v-for="message in messages" :id=message.role :key="message.id" :data="message"  />  

    <div></div>
    <div></div>




  </div>

  



  <div class="message-input">
    <textarea v-model="message" @keyup.enter="sendMessage" placeholder="Type a message" rows="1" @input="autoResize" class="message-textarea"></textarea>
    <button :disabled="!message.trim()" @click="sendMessage" class="send-button">Send</button>
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

      saveScrollPosition() {
        this.originalScrollPosition = window.scrollY;
      },

      // Restore the original scroll position when keyboard is closed
      restoreScrollPosition() {
        window.scrollTo(0, this.originalScrollPosition);
      },

      // Handle window resize and detect keyboard state change
      handleResize() {
        // If the window height is smaller than the viewport height, the keyboard is likely open
        if (window.innerHeight < this.originalHeight) {
          if (!this.isKeyboardOpen) {
            this.isKeyboardOpen = true;
            this.saveScrollPosition(); // Save scroll position when keyboard opens
            
          }
        } else {
          if (this.isKeyboardOpen) {
            this.isKeyboardOpen = false;
            this.restoreScrollPosition(); // Restore scroll position when keyboard closes
          }
        }
      },
    
      goBack() {
        this.$router.back(); // Navigate back to the Dashboard
      },
      goToChatHistory() {
        this.$router.push('/chat/history'); // Navigate to the Chat view
      },
      sendMessage() {
        const trimmedMessage = this.message.trim(); // Trim whitespace from the message

        this.messages.push({role: "user", content: trimmedMessage})

        if (!trimmedMessage) return; // Do nothing if the message is empty

        // Emit the message to the parent for immediate UI updates (optional)
        this.$emit("send-message", trimmedMessage);

        this.$nextTick(() => this.scrollToBottom());

        

        //let messageSend= {role: "user", content: trimmedMessage.toString}



        // Make the API request to send the message
        axios.post("https://iotquarium.info/api/ask-gpt", {
            role: "user",
            content: trimmedMessage, // The message content
          })
          .then((response) => {
            console.log("Message sent successfully:", response.data);

            this.messages.push({role: "assistant", content: response.data["content"]})

            this.$nextTick(() => this.scrollToBottom());

            // Optionally, you can emit the result to the parent for further handling
            this.$emit("message-sent", response.data);
          })
          .catch((error) => {
            console.error("Error sending message:", error);
          });

        // Clear the input field
        this.message = "";
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
      },

      
    },
  
   
  
    data() {
        return {
          isKeyboardOpen: false,
          originalScrollPosition: 0,
          
          messages: [
            
            { id: 1, role: "assistant", title: "Messages", content: "Loading..." },
            { id: 2, role: "user", title: "user", content: "Loading..." },
           
            
          
    
    
    
    
            ],
          message: "",
        };
      },
  
      async mounted() {


        this.originalHeight = window.innerHeight;

        // Add event listener for resize
        window.addEventListener("resize", this.handleResize);

        

        document.body.classList.add('no-scroll');
  

        this.scrollToBottom();

        
  
       
        try {

          
          const response = await axios.get('https://iotquarium.info/api/message-gpt');
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

      beforeUnmount() {
    // Enable scrolling when leaving chat view
        document.body.classList.remove('no-scroll');
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
      height: 100vh; /* Full viewport height */
      margin: 0; /* Remove default margin */

      
    }
    
   
    .no-scroll {
      overflow: hidden; /* Disable scrolling */
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

      

      

      

      border-radius: 2px;
      

      background: linear-gradient(145deg, #14cbc863, #3f4aee);

      box-shadow: 0px -10px 30px rgba(86, 86, 86, 0.407);

      
     

      margin-bottom: 0cm;
      

      

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
      background: #f5f5f534;
      color: #f5f5f5;

      
      
      font-size: 14px;
      outline: none;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    .send-button {

      top: 0.1cm;

      width: 3cm;


      margin-right: 1cm


    }



    body[data-theme="dark"] .message-input {

      
    
      background: linear-gradient(360deg, #23203694, #26264094);

     


      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);

     

    }

    body[data-theme="dark"] .message-textarea {
      
      background: #131212c4;
      color: #e6e6e6;



      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

  



    button {

      position: relative;

      text-align: center;

      




      font-weight: lighter;

      font-size: large;

      margin-right: 0.5cm;

      



      border-width: 0cm;


      /*background: linear-gradient(145deg, #14cbc894, #3f4aee);*/

      background: linear-gradient(145deg, #3d7f99b6, #51b3ddab);
      color: #ffffff;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
      border-radius: 20px;
      padding: 11px;
      
      transition: transform 0.2s ease-in-out;

      height: 1.1cm;

      width: fit-content;


      }


    body[data-theme="dark"] button {
      background: linear-gradient(195deg, #20202caf, #262a5c);
      
      color:  #fdfeff;
      box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
      
      
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
      min-height: 100%;

      

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

    margin-top: 1cm;
  
    width: fit-content;

    max-width: 40%;

    }
  
    #system {
  
    height: fit-content;

    max-height: 3cm;
  
    width: fit-content;

    max-width: 40%;

    align-self: center;

    opacity: 50%;


  
  
    }


    

    
    
  
  
    
  
  
    @media (max-width: 768px) {



      #title {

        

        height: 1.4cm;

        position: sticky;

        top: 2.3cm;

        background-color: f7f9fc;

        

        z-index: 9999;

        margin-bottom: 0.2cm;


        }

      body[data-theme="dark"] #title {


        background-color: #000000;





      }



      h2 {





        top: 0cm;
        z-index: 9999;

        height: 1.2cm;



        bottom: 0;

        }


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

        margin-left: 0.2cm;

        right: 0cm;

        overflow-x: hidden;
        /* Flexible layout */
        row-gap: 6px;
        flex-direction: column;
        min-height: 80%;
        width: 100vw;
        
        column-gap: 0px; /* Reduced column gap */
        margin-bottom: auto; /* Centers the container */
      }


      #user {
  
        align-self: center;

        height: 3cm;

        

        word-wrap: break-word;

        max-width: 40%;

        padding: 10px;

        margin-right: 0cm;

        margin-left: 3cm;



      }

        #assistant {

          align-self: unset;

          right: 0.09cm;

          margin-left: 0.3cm;

          align-self: start;

          position: relative;

          

          

          word-wrap: break-word;

          max-width: 50%;

          margin-bottom: 3cm;

          

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



          .message-input {



            width: 100vw;



          }


          .message-textarea {
           
            padding: 10px 15px;
            height: 90%;

            max-width: 100%;

            resize: none;

            font-size: 16px;

            max-height: 0.5cm;
            margin-left: 0.1cm;
            
            margin-top: 0.3cm;
            
            margin-right: 10px;
           
 
          }

          .send-button {

            margin-top: 0cm;

            margin-bottom: 0.3cm;

          }
  
  
      
  
    }
  
    @media only screen and (min-width: 768px) and (max-width: 1024px) and (orientation: portrait) {



      #title {

        

        height: 1.3cm;

        position: sticky;

        top: 2.2cm;

        background-color: #f7f9fc;

        z-index: 9999;

        margin-bottom: 0.2cm;


      }

      body[data-theme="dark"] #title {


        background: linear-gradient(180deg, #00000000, #13121200);


        }

      h2 {





        top: 0cm;
        z-index: 9999;

        height: 1.2cm;

        



        bottom: 0;

      }


      
  
     
  
     
  
      .grid-container {
  
        
  
        grid-template-columns: repeat(auto-fill, minmax(250px, 9cm));
  
        margin-bottom: 2cm
  
  
      }
  
      body {
  
        max-width: 100%;

        overflow-x: hidden;


      }

      .message-input {

        

        position: sticky;

        bottom: 1.5cm;



        padding-left: 0cm;



        align-self: center;

        }
  
    
  
    }
  
    @media only screen and (min-width: 1024px) and (max-width: 1366px) and (orientation: landscape) {

      


      #title {

        

        height: 1.3cm;

        position: sticky;

        top: 2.3cm;

        background-color: #f7f9fc;

        z-index: 9999;

        margin-bottom: 0.3cm;


      }

      h2 {

        

        

        top: 0cm;
        z-index: 9999;

        height: 1.2cm;

        

        

        

        bottom: 0;

      }

      body[data-theme="dark"] #title {


        background: linear-gradient(180deg, #00000000, #13121200);



      }


      .message-input {

        

        position: sticky;

        bottom: 1.5cm;

        

        padding-left: 0cm;

        

        align-self: center;

      }
  
     
  
      .grid-container {

      

        grid-template-columns: repeat(auto-fill, minmax(250px, 9cm));

        min-height: 100%;

      

      }
  
    
  
        
    }
  
  
  </style>
  