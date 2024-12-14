<script>
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            Id: null,
            name: null,
            ideaData: [] // 追加
        }
    },
    async created() {
        const response = await fetch(endpoint + `user/${this.$route.params.username}`)
        const data = await response.json()
        console.log(data)
        this.name = data.user.name
        this.ideaData = data.ideas // 変更
    },
}

</script>
<template>
    <div>
        <div class="top">
            <div class="icon"></div>
            <h1>{{ name }}</h1>
        </div>
        <div class="timeLine">
            <div v-for="id in ideaData" :key="id" class="postContents">
                <PostView class="postView" :id="id" />
            </div>
        </div>
    </div>
</template>
<style scoped>
.top {
    display: flex;
    padding: 10px;
}
h1 {
    margin: 0px;
    padding: 0px;
    margin-left: 20px;
}
.icon {
    width: 40px;
    height: 40px;
    background-color: black;
    border-radius: 50%;
}
.timeLine {
    padding: 10px;
    background-color: #f3f3f3;
    display:flex;
    flex-wrap:wrap;
}
.postContents {
    width: 50%;
}
.postView {
    margin: 5%;
}
</style>