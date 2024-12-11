<template>
    <top>{{ title }}</top>
        <img src="assets/sampleImage1.jpeg" alt="サムネイル" class="image">
        <div class="profile">
            <img src="https://via.placeholder.com/40" alt="アイコン">
            <span>{{ username }}</span> <!-- ユーザーIDを表示 -->
        </div>
    <main class="content">
        <p>サンプル本文5000兆円ほしいああああああああああああああああああああ</p>
    </main>
    <bottom>
        <img src="assets/comment.png" alt="comment" >
        <img src="assets/fork.png" alt="fork" >
        <img src="assets/heart.png" alt="heart" >
        <img src="assets/light.png" alt="light" >
    </bottom >

</template>

<script>
export default {
    data() {
        return {
            title: '',
            fork: null,
            user_id: null,
        }
    },
    async created() {
        const response = await fetch(`http://10.124.75.43:8000/api/ideas/${this.$route.params.id}`)
        const data = await response.json()
        this.title = data.idea.title
        this.fork = data.idea.fork
        this.username = data.username
    },
}
</script>

<style scoped>
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
    font-size: 24px;
    font-weight: bold;
    padding: 20px 0;
    background-color: #fff;
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px 20px;
}

bottom {
    border-top: 1px solid #333;
    display: flex;
    margin:5px;
    padding-top: 10px;
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
    display: flex;
    align-items: center;
    padding: 10px 20px;
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
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
    font-size: 16px;
    line-height: 1.5;
}
</style>