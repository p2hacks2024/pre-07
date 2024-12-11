<script>
import PostView from '@/components/PostView.vue'

export default {
    data() {
        return {
            ids: []
        }
    },
    async created() {
        const response = await fetch('http://10.124.75.43:8000/api/ideas/')
        const data = await response.json()
        this.ids = data
    },
}
</script>

<template>
    <div class="timeLine">
        <div v-for="id in ids" :key="id" class="postContents">
            <PostView class="postView" :id="id"/>
        </div>
    </div>
</template>

<style>
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