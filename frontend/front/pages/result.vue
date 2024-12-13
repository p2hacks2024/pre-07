<script>
import PostView from '@/components/PostView.vue'
import { endpoint } from '~/components/APIEndPoint';

export default {
    data() {
        return {
            ids: []
        }
    },
    async created() {
        const response = await fetch(endpoint + 'ideas/')
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

<style scoped>
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