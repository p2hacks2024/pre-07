<template>
  <div id="app">
    <header>
      <h1>Simple Post App</h1>
    </header>
    <main>
      <PostForm @submit="handlePost" />
      <section v-if="postHistory.length > 0" class="post-history">
        <h2>投稿履歴</h2>
        <div class="post-grid">
          <div v-for="(post, index) in postHistory" :key="index" class="post-item">
            <div class="user-info">
              <UserAvatar :user="post.user" />
              <p><strong>{{ post.user.name }}</strong></p>
            </div>
            <p><strong>投稿内容:</strong> {{ post.content }}</p>
            <MediaDisplay :media="post.media" :mediaType="post.mediaType" />
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import PostForm from "/components/PostForm.vue";
import MediaDisplay from "/components/MediaDisplay.vue";
import UserAvatar from "/components/UserAvatar.vue";

export default {
  components: {
    PostForm,
    MediaDisplay,
    UserAvatar,
  },
  data() {
    return {
      postHistory: [], // 投稿履歴を保存
    };
  },
  methods: {
    handlePost(formData) {
      const user = {
        name: "Example User", // ユーザー名をダミーデータとして挿入
        avatar: "https://via.placeholder.com/40", // ダミーアバター画像
      };

      if (formData.get("file")) {
        const file = formData.get("file");
        const reader = new FileReader();
        reader.onload = (e) => {
          this.postHistory.push({
            user,
            content: formData.get("content"),
            media: e.target.result,
            mediaType: file.type.startsWith("image") ? "image" : "video",
          });
        };
        reader.readAsDataURL(file);
      } else {
        this.postHistory.push({
          user,
          content: formData.get("content"),
          media: null,
          mediaType: null,
        });
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}
header {
  text-align: center;
  margin-bottom: 20px;
}
.post-history {
  margin-top: 20px;
}
.post-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.post-item {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 10px;
  width: 100%;
  box-sizing: border-box;
  background: #f9f9f9;
}
@media (min-width: 600px) {
  .post-item {
    width: calc(50% - 10px);
  }
}
.user-info {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.user-info p {
  margin-left: 10px;
}
.post-item img,
.post-item video {
  max-width: 100%;
  border-radius: 4px;
  margin-top: 10px;
}
</style>
