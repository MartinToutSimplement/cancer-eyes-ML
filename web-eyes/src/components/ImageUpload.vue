<template>
    <div>
      <input type="file" id="fileUpload" ref="fileInput" @change="uploadImage" style="display: none" />
      <center>
      <label for="fileUpload" class="upload-btn">Upload your file</label>
    </center>

      <span v-if="result"> Diagnosis: {{ result }} </span>
      <div v-if="uploadedImage">
        <img :src="uploadedImage" alt="Uploaded Eye" width="150" />
      </div>
      <div v-if="result" class="result-container">
        <div class="progress-bar">
            <div class="progress-fill" :style="{ width: (result * 100) + '%' }">
                <!-- <span class="percentage-label">{{ (result * 100).toFixed(0) }}%</span> -->
            </div>
        </div>
        <span class="resultspan" v-if="result >= 0.75">The result suggests a Non-cancerous condition with a confidence of {{ (result * 100).toFixed(2) }}%.</span>
        <span class="resultspan" v-else>The result suggests a Cancerous condition with a confidence of {{ ((1 - result) * 100).toFixed(2) }}%. <br> We advise you to consult a doctor for further clarification.</span>
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
        this.$emit('imageUploaded');
        this.$emit('imageUploaded');
  
        try {
          const response = await axios.post('http://localhost:5000/predict', formData);
        //   this.result = response.data.result === "1" ? "Cancéreux" : "Non cancéreux";
          this.result = response.data.result;
          console.log(this.result)
          this.uploadedImage = URL.createObjectURL(imageFile);
        } catch (error) {
          console.error("Error during the diagnosis:", error);
        }
      }
    }
  };
  </script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Arial', sans-serif;
}

.resultspan{
  color: #FFF;
  font-weight: 700;
  text-align: center;
}

.upload-btn {
  display: inline-block;
  padding: 20px 40px;
  background: linear-gradient(45deg, #6AB1D7, #33D9B2);
  color: #FFF;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 700;
  font-size: 20px;
  box-shadow: 0px 4px 30px rgba(0,0,0,0.2);
  text-align: center;
  text-decoration: none;
  outline: none;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.upload-btn:before, .upload-btn:after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.2);
  z-index: 1;
  transform: scale(0);
  transition: all 0.5s;
}

.upload-btn:hover {
  box-shadow: 0px 6px 45px rgba(0,0,0,0.25);
  transform: translateY(-5px);
}

.upload-btn:hover:before {
  transform: scale(1.5);
  opacity: 0;
}

.upload-btn:after {
  animation: wave-animation 2.5s infinite;
  opacity: 0.4;
}

@keyframes wave-animation {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

img {
  max-width: 100%;
  max-height: 400px;
  display: block;
  margin: 0 auto;
  border-radius: 8px;
  max-width: 100%;
  max-height: 400px;
  display: block;
  margin: 0 auto;
  border-radius: 8px;
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

div[v-if="uploadedImage"] {
  max-width: 100%;
  overflow-y: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 24px;
  padding: 16px;
  background-color: rgba(255, 255, 255, 0.1);
}

div[v-if="uploadedImage"] {
  max-width: 100%;
  overflow-y: auto;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 24px;
  padding: 16px;
  background-color: rgba(255, 255, 255, 0.1);
}
.result-container {
    margin-top: 30px;
}

.progress-bar {
    background-color: #e0e0e0;
    border-radius: 12px;
    height: 30px;
    overflow: hidden;
}

.progress-fill {
    background: linear-gradient(45deg, #6AB1D7, #33D9B2);
    height: 100%;
    transition: width 0.5s ease-in-out;
}
.percentage-label {
    color: #FFF;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    position: absolute;
}
</style>
