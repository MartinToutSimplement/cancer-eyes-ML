<template>
  <div>
    <h1>Vue.js Frontend</h1>
    <button @click="fetchMessage">Get Message from Flask</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: ''
    };
  },
  methods: {
    async fetchMessage() {
      try {
        const response = await axios.get('/api/message');
        this.message = response.data.message;
      } catch (error) {
        console.error('There was an error:', error.response);
      }
    }
  }
}
</script>
