<template>
    <div>
        <h2>Upload an eye file for the analysis</h2>
      <!-- Hide the original input and add a label to act as the button -->
      <input type="file" id="fileUpload" ref="fileInput" @change="uploadImage" style="display: none" />
      <center>
      <label for="fileUpload" class="upload-btn">Upload your file</label>
    </center>

      <span v-if="result"> Diagnosis: {{ result }} </span>
      <div v-if="uploadedImage">
        <img :src="uploadedImage" alt="Uploaded Eye" width="150" />
      </div>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        uploadedImage: null,
        result: null
      };
    },
    methods: {
      async uploadImage() {
        const imageFile = this.$refs.fileInput.files[0];
        const formData = new FormData();
        formData.append('file', imageFile);
  
        try {
          const response = await axios.post('http://localhost:5000/predict', formData);
        //   this.result = response.data.result === "1" ? "Cancéreux" : "Non cancéreux";
          this.result = response.data.result;
          this.uploadedImage = URL.createObjectURL(imageFile);
        } catch (error) {
          console.error("Error during the diagnosis:", error);
        }
      }
    }
  };
  </script>

<style>
/* Base styling */
* {
  box-sizing: border-box;
  font-family: 'Arial', sans-serif;
}

/* Styling the label to look like a modern button */
.upload-btn {
  display: inline-block;
  padding: 20px 40px;  /* Increased padding for a bigger button */
  background: linear-gradient(45deg, #6AB1D7, #33D9B2);  /* Gradient background */
  color: #FFF;
  border: none;
  border-radius: 50px;  /* Very rounded corners */
  cursor: pointer;
  font-weight: 700;  /* Extra bold */
  font-size: 20px;  /* Bigger font size */
  box-shadow: 0px 4px 30px rgba(0,0,0,0.2);  /* Noticeable shadow */
  text-align: center;
  text-decoration: none;
  outline: none;
  transition: all 0.3s ease;
  position: relative;  /* For pseudo-elements */
  overflow: hidden;  /* Clip the overflowing parts of the pseudo-elements */
}

/* Adding pseudo-elements for additional animation layers */
.upload-btn:before, .upload-btn:after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.2);  /* Slight white tint */
  z-index: 1;
  transform: scale(0);
  transition: all 0.5s;
}

/* Hover animations */
.upload-btn:hover {
  box-shadow: 0px 6px 45px rgba(0,0,0,0.25);  /* Intensified shadow */
  transform: translateY(-5px);  /* Lift up effect */
}

.upload-btn:hover:before {
  transform: scale(1.5);
  opacity: 0;
}

.upload-btn:after {
  animation: wave-animation 2.5s infinite;
  opacity: 0.4;
}

/* Keyframes for a wave effect */
@keyframes wave-animation {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

/* Styling for image and text */
img {
  border-radius: 8px;
  margin-top: 24px;
}

span {
  display: block;
  margin-top: 24px;
  font-size: 22px;
  font-weight: bold;
}

h2 {
  font-size: 3em;
  color: #fff;
  margin-bottom: 10px;
}


</style>
