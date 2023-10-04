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

  <body>
    

  <header>

  </header>

  <section class="parallax">
    <img src="science.jpg" id="science">
    <h2 id="text" ref="parallaxText"> Eye Cancer Project</h2>

  </section>

  <section class="sec">
    <h2>Parallax Scrolling Website</h2>
    <p>

      
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. 
      Nihil possimus consequatur soluta, labore nisi molestias aut dolor, velit, sequi cumque vel vero! 
      Alias eius, unde corporis error natus ex provident! <br><br>
    </p>
  </section>

</body>
</div>
</template>

<script>
export default {
  data() {
    return {
      scrollPosition: 0
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeMount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.scrollPosition = window.scrollY;

      if (!this.$refs.parallaxText) {
    console.error("The parallaxText element is missing!");
    return;
  }

      // Adjust these values based on your design and preference
      const maxScroll = 800; // Maximum scroll value where the effect ends
      const fadeStart = 400; // Scroll value where the fade effect starts

      if (this.scrollPosition <= maxScroll) {
        const translateYValue = this.scrollPosition * 1; // Adjust the multiplier for more or less movement
        const opacityValue = this.scrollPosition >= fadeStart ? 1 - (this.scrollPosition - fadeStart) / (maxScroll - fadeStart) : 1;

        this.$refs.parallaxText.style.transform = `translateY(${translateYValue}px)`;
        this.$refs.parallaxText.style.opacity = opacityValue;
      }
    }
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
  justify-content: flex-start;
  align-items: center;
  z-index: 100;
}

.logo {
  font-size: 2em;
  color: #359381;
  pointer-events: none;
  margin-right: 270px;
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
  color: #fff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  opacity: 0;
  animation: fadeIn 1s forwards 1s; /* 2s duration, starts after 1s delay */
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.parallax img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  pointer-events: none;
}

.sec {
  position: relative;
  background: #003329;
  padding: 100px;
}

.sec h2 {
  font-size: 3em;
  color: #fff;
  margin-bottom: 10px;
}

.sec p {
  font-size: 1em;
  color: #fff;
  font-weight: 300;
}

</style>
