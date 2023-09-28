<template>
  <div id="app">
    <header>
      Web-Eyes
    </header>
    <ImageUpload />
  </div>
</template>

<script>
import ImageUpload from './components/ImageUpload.vue';

export default {
  components: {
    ImageUpload
  }
};
</script>

<style>
/* Global styles pour un design épuré */
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}
header {
  background-color: #2c3e50;
  color: white;
  font-size: 24px;
  padding: 20px 0;
  text-align: center;
}
</style>
