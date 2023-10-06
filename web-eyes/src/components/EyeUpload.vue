<template>
  <div class="zoom-container">
    <img :style="{transform: `scale(${scale})`}" src="oeil.jpg" alt="Zoomable Image" class="zoom-image">
    <div :style="{opacity: fadeOpacity}" class="fade-overlay">
      <ImageUpload :style="{opacity: imageUploadOpacity}" class="centered-upload"/>

    </div>
  </div>
</template>

<style scoped>
.zoom-container {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
}

.zoom-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
  z-index: 1;
  max-height: none;
}

.fade-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  transition: opacity 0.3s ease;
  z-index: 2;
}
.centered-upload {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0; /* Par défaut, il sera transparent */
  transition: opacity 0.3s ease; /* Ajout d'une transition pour l'opacité */
}



</style>

<script>
import ImageUpload from './ImageUpload.vue';
export default {
  components: {
    // ImageUploader,
    ImageUpload
  },
  data() {
  return {
    scale: 1,
    fadeOpacity: 0,
    imageUploadOpacity: 0

  };
},
methods: {
  handleScroll(event) {
    const scrollPosition = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100;
    
    if (scrollPosition > 80) {
      const direction = event.deltaY > 0 ? 1 : -1;
      this.scale = direction > 0 ? this.scale * 1.05 : this.scale / 1.05;

      if (this.scale < 1) this.scale = 1;

      if (this.scale >= 3) {
        this.scale = 3;
        this.fadeOpacity = 1;
        this.imageUploadOpacity = 1; // Afficher ImageUpload une fois le fondu complet.
      } else {
        this.fadeOpacity = (this.scale - 1) / 2;
        this.imageUploadOpacity = 0; // Cacher ImageUpload lors du dézoom.
      }

    } else {
      if (this.scale !== 1) {
        this.scale = 1;
      }
      this.fadeOpacity = 0;
      this.imageUploadOpacity = 0; // Cacher ImageUpload lors du remontage.
    }
  }
},

  mounted() {
    window.addEventListener('wheel', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('wheel', this.handleScroll);
  }
};
</script>



