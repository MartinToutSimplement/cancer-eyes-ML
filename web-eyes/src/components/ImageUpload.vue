<template>
    <div class="image-upload">
      <label for="imageInput" v-if="!imageSrc">
        Cliquez ici ou déposez une image
        <input type="file" id="imageInput" @change="onImageChange" />
      </label>
      <div v-if="imageSrc">
        <img :src="imageSrc" alt="Uploaded preview" class="preview-image" />
        <button class="submit-button" @click="sendImage">Envoyer</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        imageSrc: null
      };
    },
    methods: {
      onImageChange(event) {
        const file = event.target.files[0];
        this.imageSrc = URL.createObjectURL(file);
      },
      sendImage() {
        // Vous pouvez gérer l'envoi de l'image ici
        console.log("Image envoyée!");
      }
    }
  };
  </script>
  
  <style scoped>
  .image-upload {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
  label {
    cursor: pointer;
  }
  
  input[type="file"] {
    display: none;
  }
  
  .preview-image {
    max-width: 300px;
    margin-top: 20px;
  }

  .submit-button {
  margin-top: 20px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #3498db;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #2980b9;
}

  </style>
  