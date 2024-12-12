<template>
    <top>{{ title }}</top>
    <img src="assets/sampleImage1.jpeg" alt="サムネイル" class="image">
    <router-link class="profile" :to="`/${username}`">
        <img src="https://via.placeholder.com/40" alt="アイコン">
        <span>{{ username }}</span> <!-- ユーザーIDを表示 -->
    </router-link>
    <main class="content">
        <p>{{ content }}</p>
    </main>
    <bottom>
        <img src="assets/comment.png" alt="comment">
        <img src="assets/fork.png" alt="fork">
        <img src="assets/heart.png" alt="heart">
        <img src="assets/light.png" alt="light">
    </bottom>

</template>

<script>
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            title: '',
            fork: null,
            user_id: null,
        }
    },
    async created() {
        const response = await fetch(endpoint + `ideas/${this.$route.params.id}`)
        const data = await response.json()
        this.title = data.idea.title
        this.content = data.idea.content
        this.username = data.username
    },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New&display=swap');

.content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}
top {
    font-family: "Zen Kaku Gothic New", sans-serif;
    font-size: 24px;
    font-weight: bold;
    padding: 20px 0;
    background-color: #fff;
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 20px;
}

bottom {
    border-top: 1px solid #a2a2a2;
    background-color: #fff;
    display: flex;
    position: fixed;
    left: 0px;
    bottom: 60px;
    width: 100%;
    padding-top: 10px;
    padding-bottom: 15px;
    justify-content: space-around;
}

bottom img {
    width: 30px;
    height: 30px;
    display: block;
}

.image {
    width: 100%;
    height: auto;
}

.profile {
    font-family: "Zen Kaku Gothic New", sans-serif;
    display: flex;
    align-items: center;
    padding: 10px 40px;
    border-bottom: 1px solid #ddd;
    text-decoration: none;
    color: #000;
}

.profile img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 15px;
}

main {
    padding: 40px;
}

h1 {
    font-size: 24px;
    margin-bottom: 15px;
}

p {
    font-family: "Zen Kaku Gothic New", sans-serif;
    font-size: 16px;
    line-height: 1.5;
}
</style>