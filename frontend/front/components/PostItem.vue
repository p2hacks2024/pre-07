
<template>
  <div class="post-item">
    <div class="user-info">
      <img :src="post.user.avatar" alt="User Avatar" class="user-avatar" />
      <span class="user-name">{{ post.user.name }}</span>
      <span class="post-date">{{ formattedDate }}</span>
    </div>
    <p class="post-content">{{ post.content }}</p>
    <div v-if="post.media" class="post-media">
      <img v-if="isImage" :src="post.media" alt="Post Media" />
      <video v-if="isVideo" controls :src="post.media"></video>
    </div>
    <div class="post-actions">
      <button @click="likePost">{{ post.likes }} ❤️</button>
      <button @click="$emit('comment', post.id)">💬</button>
      <button @click="$emit('share', post.id)">🔗</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  computed: {
    formattedDate() {
      return new Date(this.post.date).toLocaleString();
    },
    isImage() {
      return this.post.media && this.post.mediaType === "image";
    },
    isVideo() {
      return this.post.media && this.post.mediaType === "video";
    },
  },
  methods: {
    likePost() {
      this.$emit("like", this.post.id);
    },
  },
};
</script>

<style>
.post-item {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}
.user-info {
  display: flex;
  align-items: center;
}
.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}
.user-name {
  font-weight: bold;
}
.post-content {
  margin-top: 5px;
  white-space: pre-wrap;
}
.post-media img,
.post-media video {
  max-width: 100%;
  margin-top: 10px;
}
.post-actions button {
  margin-right: 10px;
  cursor: pointer;
  border: none;
  background: none;
  font-size: 14px;
}
</style>
