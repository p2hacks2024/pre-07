<template>
  <div class="post-form">
    <textarea
      v-model="postContent"
      :maxlength="maxLength"
      placeholder="今どうしてる？"
      class="post-textarea"
    ></textarea>
    <div class="post-actions">
      <input type="file" @change="handleFileUpload" accept="image/*,video/*" class="file-input" />
      <span class="char-counter">{{ postContent.length }}/{{ maxLength }}</span>
      <button :disabled="!canSubmit" @click="submitPost">投稿する</button>
    </div>
    <div v-if="preview" class="preview">
      <img v-if="isImage" :src="preview" alt="Preview" />
      <video v-if="isVideo" controls :src="preview"></video>
      <button @click="clearFile">×</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      postContent: "",
      file: null,
      preview: null,
      maxLength: 280,
    };
  },
  computed: {
    canSubmit() {
      return this.postContent.trim().length > 0 || this.file;
    },
    isImage() {
      return this.file && this.file.type.startsWith("image");
    },
    isVideo() {
      return this.file && this.file.type.startsWith("video");
    },
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.file = file;
        this.preview = URL.createObjectURL(file);
      }
    },
    clearFile() {
      this.file = null;
      this.preview = null;
    },
    submitPost() {
      const formData = new FormData();
      formData.append("content", this.postContent);
      if (this.file) {
        formData.append("file", this.file);
      }

      this.$emit("submit", formData); // 親コンポーネントへ送信
      this.postContent = "";
      this.clearFile();
    },
  },
};
</script>

<style>
.post-form {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 8px;
}
.post-textarea {
  width: 100%;
  height: 80px;
  resize: none;
}
.post-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}
.char-counter {
  font-size: 12px;
  color: gray;
}
.preview {
  margin-top: 10px;
  position: relative;
}
.preview img,
.preview video {
  max-width: 100%;
  border-radius: 8px;
}
.preview button {
  position: absolute;
  top: 5px;
  right: 5px;
  background: red;
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
}
</style>
