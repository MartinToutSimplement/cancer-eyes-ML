<template>

  <div class="main">
  <div>

    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, intial-scale=1.0">
      <title>Parallax Scrolling Website | Codehal</title>
      <link rel="stylesheet" href="style.css">
    </head>
  </div>

  <header>
    <h2 class="logo">Logo</h2>
    <nav class="navigation">
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Service</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <section class="parallax">
    <h2 id="text"> Parallax Website</h2>
  </section>

  <!-- <div class="bouton">
    <ImageUpload />
  </div> -->
</div>
</template>

<script>
import ImageUpload from './components/ImageUpload.vue';

export default {
  name: 'App',
  components: {
    ImageUpload
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  background-color: #f9f9f9;
  min-height: 100vh;
  overflow-x: hidden;
}

header {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  padding: 30px 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
}

.logo {
  font-size: 2em;
  color: #359381;
  pointer-events: none;
}

.navigation a {
  text-decoration: none;
  color: #359381;
  padding: 6px 15px;
  border-radius: 20px;
  margin: 0 10px;
  font-weight: 600;
}

.navigation a:hover {
  background-color: #359381;
  color: #fff;
}

.navigation a.active {
  background-color: #359381;
  color: #fff;
}

.parallax {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

#text {
  position: absolute;
  font-size: 5em;
  color: #359381;
}
</style>
