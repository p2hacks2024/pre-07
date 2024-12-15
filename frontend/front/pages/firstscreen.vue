<template>
  <div class="container">
    <div class="logo-container">
      <img src="@/assets/logo.png" class="logo" />
    </div>
    <div class="loading-bar-container">
      <div class="loading-bar"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FirstScreen',
  mounted() {
    this.animateLogo();
    this.animateLoadingBar();
  },
  methods: {
    animateLogo() {
      const logo = this.$el.querySelector('.logo');
      logo.style.opacity = 0;
      setTimeout(() => {
        logo.style.transition = 'opacity 2s';
        logo.style.opacity = 1;
      }, 100);
    },
    animateLoadingBar() {
      const loadingBar = this.$el.querySelector('.loading-bar');
      const speed = 3000; // ローディングバーのスピード（ミリ秒）
      loadingBar.style.width = '0%';
      setTimeout(() => {
        loadingBar.style.transition = `width ${speed}ms`;
        loadingBar.style.width = '100%';
      }, 100);
      setTimeout(() => {
        this.$router.push('/home');
      }, speed + 100);
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #fff7a1;
}
.logo-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo {
  width: 150px; /* 以前の100pxから変更 */
  height: auto; /* 以前の100pxから変更 */
  margin-top: -50px; /* ロゴを上に移動 */
}
.loading-bar-container {
  width: 80%;
  height: 10px;
  background-color: #fff;
  border-radius: 5px;
  margin-bottom: 50px;
  position: absolute;
  bottom: 20px;
}
.loading-bar {
  width: 0%;
  height: 100%;
  background-color: #fbd240;
  border-radius: 5px;
}
footer {
  display: none;
}
</style>