<template>
  <div class="zoom-container">
    <img :style="{transform: `scale(${scale})`}" src="oeil.jpg" alt="Zoomable Image" class="zoom-image">
    <div class="scroll-instruction">Scroll down</div>
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
  transform-origin: 55% 40%;
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

.scroll-instruction {
  position: absolute;
  bottom: 20px; /* Adjust as needed */
  left: 50%;
  transform: translateX(-50%);
  color: white;
  font-size: 18px; /* Adjust as needed */
  opacity: 1; 
  transition: opacity 0.3s ease;
  z-index: 2; /* To make sure it's above the image but below the overlay */
}


</style>

<script>
import ImageUpload from './ImageUpload.vue';

export default {
  components: {
    ImageUpload
  },
  data() {
    return {
      scale: 1,
      fadeOpacity: 0,
      imageUploadOpacity: 0,
      instructionOpacity: 1
    };
  },
  methods: {
    handleScroll(event) {
      const scrollPosition = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100;

      if (scrollPosition > 90) {
        const direction = event.deltaY > 0 ? 1 : -1;
        this.scale = direction > 0 ? this.scale * 1.25 : this.scale / 1.25;

        if (this.scale < 1) this.scale = 1;

        if (this.scale >= 4) {
          this.scale = 4;
          this.fadeOpacity = 1;
          this.imageUploadOpacity = 1;
          this.instructionOpacity = 0; // Hide instruction text
        } else {
          this.fadeOpacity = (this.scale - 2) / 2;
          this.imageUploadOpacity = 0;
          this.instructionOpacity = 1 - (this.scale - 1) / 2; // Adjust instruction opacity based on scale
        }

      } else {
        if (this.scale !== 1) {
          this.scale = 1;
        }
        this.fadeOpacity = 0;
        this.imageUploadOpacity = 0;
        this.instructionOpacity = 1; // Show instruction text
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




