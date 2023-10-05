<template>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
  <div id="app">
    <nav>
  <div class="nav-container">
    <a href="#" class="brand">Eye Cancer Project</a>
    <ul class="nav-links">
      <li><a href="#section1">Home</a></li>
      <li><a href="#section2">Upload</a></li>
      <!-- Vous pouvez ajouter d'autres liens ici si nécessaire -->
    </ul>
  </div>
</nav>


    <!-- Section 1 -->
    <section id="section1">
  <transition name="fade">
    <h1 v-if="showProjectTitle" @click="toggleContent" class="fade-in">Eye Cancer Project</h1>
    <p v-else @click="toggleContent">Your paragraph content here...</p>
  </transition>
</section>

    <!-- Section 2 -->
    <section id="section2">
      <h1>Upload an eye file for the analysis</h1>
      <template v-if="!imageIsUploaded">
      <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
        Ad iure asperiores porro quidem harum voluptate velit illum maxime quas, modi earum! Nostrum doloremque aliquam, 
        laudantium veritatis asperiores amet dolore veniam.</p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
        Ad iure asperiores porro quidem harum voluptate velit illum maxime quas, modi earum! Nostrum doloremque aliquam, 
        laudantium veritatis asperiores amet dolore veniam.</p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
        Ad iure asperiores porro quidem harum voluptate velit illum maxime quas, modi earum! Nostrum doloremque aliquam, 
        laudantium veritatis asperiores amet dolore veniam.</p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
        Ad iure asperiores porro quidem harum voluptate velit illum maxime quas, modi earum! Nostrum doloremque aliquam, 
        laudantium veritatis asperiores amet dolore veniam.</p>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. 
        Ad iure asperiores porro quidem harum voluptate velit illum maxime quas, modi earum! Nostrum doloremque aliquam, 
        laudantium veritatis asperiores amet dolore veniam.</p>
      </template>
      <ImageUploader @imageUploaded="handleImageUpload" />
    </section>
  </div>
</template>

<script>
import ImageUploader from './components/ImageUpload.vue';
export default {
  name: 'App',
  components: {
    ImageUploader
  },
  data() {
    return {
      showParagraph: false,
      showGif: false,
      imageIsUploaded: false,
      showProjectTitle: true
    };
  },
  methods: {
    toggleContent() {
      this.showProjectTitle = !this.showProjectTitle;
    },
    handleImageUpload() {
      this.imageIsUploaded = true;
    }
  }
}
</script>


<style scoped>
/* Styles globaux */

body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  overflow-x: hidden;
  line-height: 1.6;
  background-color: #f4f4f4;
}

#app {
  width: 100%;
  background: linear-gradient(to bottom, #8AB0AB, #3E505B, #26413C, #1A1D1A, #03120E);
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 15px 20px;
  background-color: rgba(10, 10, 10, 0.95); /* Fond presque opaque */
  backdrop-filter: blur(10px); /* Effet de flou pour le fond */
  z-index: 1000;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); /* Ombre douce en bas */
  transition: background-color 0.3s ease;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand {
  color: var(--primary-color);
  font-size: 1.7em;
  text-decoration: none;
  font-weight: 700;
  letter-spacing: 1px; /* Espacement des lettres pour un look premium */
  transition: color 0.3s ease;
}

.brand:hover {
  color: #fff; /* Changement de couleur au survol */
}

.nav-links {
  list-style: none;
  padding: 0;
  display: flex;
  gap: 25px;
}

.nav-links li a {
  color: white;
  text-decoration: none;
  font-weight: 500; /* Poids de police semi-gras */
  padding: 5px 10px; /* Espacement autour des liens pour un meilleur toucher/clic */
  border-radius: 5px; /* Coins arrondis pour les effets de survol */
  transition: background-color 0.3s ease, color 0.3s ease;
}

.nav-links li a:hover {
  background-color: var(--primary-color); /* Fond doré au survol */
  color: #000; /* Texte noir au survol */
}

/* Pour les écrans plus petits, augmentez la taille des liens pour une meilleure expérience tactile */
@media (max-width: 768px) {
  .nav-links li a {
    padding: 10px 15px;
    font-size: 1.1em;
  }
}

section {
  width: 100%;
  min-height: 100vh; /* Changed from height to min-height */
  padding: 60px 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  transition: background-color 1s, transform 0.5s;
  background-color: rgba(255, 255, 255, 0.05);
  border-bottom: 3px solid rgba(255, 255, 255, 0.1);
  position: relative; /* Added for potential absolute positioned children */
}

section:hover {
  transform: scale(1.02);
  background-color: rgba(255, 255, 255, 0.08);
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.05));
}

h1 {
  font-size: 5em;
  margin-bottom: 30px;
  cursor: pointer;
  color: #fff;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
  transition: transform 0.3s ease, color 0.3s;
  font-family: 'Roboto', sans-serif;
  font-weight: 900; /* Utilisation d'un poids de police plus lourd pour un impact visuel */
}

h1:hover {
  transform: scale(1.08);
  color: #FFD700; /* Gold */
}

p {
  font-weight: 300;
  max-width: 800px;
  text-align: justify;
  margin-bottom: 30px;
  background: rgba(255, 255, 255, 0.1);
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: background 0.3s, transform 0.3s; /* Added transition */

  &:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: translateY(-5px);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

html {
  scroll-behavior: smooth;
}

.fade-enter-active, .fade-leave-active {
  transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1), opacity 0.5s, color 0.5s;
  /* perspective: 1000px; */
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
  transform: scale(0.9) rotateX(10deg);
  color: #FFD700; /* Gold */
}
</style>
