<template>
    <div v-if="showInitialMessage" class="topText">
        <p>他の人のアイディアを<br>
        見てみましょう</p><br>
    </div>
    <div class="search">
        <input
        type="text"
        id="serchText"
        placeholder="アイデアを検索"
        v-model="keyword"
        @keyup.enter="search"
        >
    </div>
    <div v-if="noIdea" class="topText">
        <p>アイデアが見つかりませんでした</p>
    </div>
    <div class="timeLine">
        <div v-for="id in ids" :key="id" class="postContents">
            <PostView class="postView" :id="id"/>
        </div>
    </div>
</template>

<script>
import PostView from '@/components/PostView.vue'
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            keyword: '',
            ids: [],
            noIdea: false,
            showInitialMessage: true
        }
    },
    methods: {
        async search() {
            this.showInitialMessage = false
            const response = await fetch(endpoint + 'search/?keyword=' + this.keyword)
            const data = await response.json()
            this.ids = data
            console.log(this.ids)
            this.noIdea = this.ids.length === 0
        }
    },
    mounted() {
        this.showInitialMessage = true
    }
}

</script>


<style scoped>

p{
    text-align: center;
}
.topText{
    padding: 50px;
    margin-top: 50px;
}
.timeLine {
    padding: 10px;
    background-color: #ffffff;
}
.postContents {
    width: flex;
}
.postView {
    margin: 5%;
}
.textBox{
    margin: 5%;
}
.search {
    text-align: center;
    margin: 5%;
    margin-top: 100px; /* ヘッダーにかぶらないようにマージンを追加 */
}
.search input {
    font-size: 16px;
    border: 1px solid #fff;
    background-color: rgb(224, 224, 224);
    padding: 15px 30px;
    border-radius: 15px;
    width: 60%;
}
</style>
