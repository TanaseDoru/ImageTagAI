<template>
  <div id="app">
    <div class="container">
      <h1>Image Tagging</h1>

      <div class="upload-section">
        <input type="file" @change="handleFileChange" accept="image/*" />
        <button @click="uploadImage" :disabled="!file">Procesează</button>
      </div>

      <div v-if="currentImage.url" class="preview-card">
        <img :src="currentImage.url" alt="Preview" />
        <div class="tags-list">
          <h2>Tag-uri găsite:</h2>
          <ul>
            <li v-for="(tag, i) in currentImage.tags" :key="i">
              {{ tag.name }} — {{ (tag.confidence * 100).toFixed(1) }}%
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      currentImage: { url: '', tags: [] }
    };
  },
  methods: {
    handleFileChange(e) {
      this.file = e.target.files[0];
      // Reset preview
      this.currentImage = { url: '', tags: [] };
    },
    async uploadImage() {
      if (!this.file) return;

      const form = new FormData();
      form.append('file', this.file);
      const api = import.meta.env.VITE_API_URL || 'http://localhost:8000';

      try {
        const { data } = await axios.post(`${api}/upload`, form);
        this.currentImage.url = data.url;
        this.currentImage.tags = data.tags;
        this.file = null;
      } catch (err) {
        console.error('Upload error:', err);
      }
    }
  }
};
</script>

<style>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: #f0f2f5;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.container {
  background: #fff;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
  text-align: center;
}
h1 {
  margin-bottom: 1.5rem;
  color: #333;
}
.upload-section {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}
.upload-section input[type='file'] {
  flex: 1;
}
.upload-section button {
  background: #0078d7;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s;
}
.upload-section button:disabled {
  background: #a0a0a0;
  cursor: not-allowed;
}
.upload-section button:not(:disabled):hover {
  background: #005fa3;
}
.preview-card {
  margin-top: 2rem;
  text-align: left;
}
.preview-card img {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 1rem;
}
.tags-list h2 {
  margin-bottom: 0.5rem;
  color: #444;
}
.tags-list ul {
  list-style: none;
  padding: 0;
}
.tags-list li {
  background: #e1f5fe;
  margin-bottom: 0.4rem;
  padding: 0.5rem;
  border-radius: 4px;
  color: #0277bd;
}
</style>
