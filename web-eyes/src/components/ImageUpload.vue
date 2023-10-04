<template>
    <div>
      <input type="file" ref="fileInput" @change="uploadImage" />
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
  