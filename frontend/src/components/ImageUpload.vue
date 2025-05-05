
<template>
  <div class="upload-container">
    <h2>Upload imagine pentru tagging</h2>
    <input type="file" @change="onFileChange" />
    <button @click="uploadFile">Trimite</button>
    <ul>
      <li v-for="(tag, index) in tags" :key="index">
        {{ tag.name }} - {{ tag.confidence }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      tags: []
    };
  },
  methods: {
    onFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async uploadFile() {
      const formData = new FormData();
      formData.append("file", this.selectedFile);

      const response = await fetch("http://localhost:3000/upload", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      this.tags = data.tags;
    }
  }
};
</script>

<style scoped>
.upload-container {
  padding: 20px;
}
</style>
