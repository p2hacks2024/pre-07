<script>
import PostView from '@/components/PostView.vue'
import { endpoint } from '~/components/APIEndPoint';
import MovePostviewButton from '~/components/movePostviewButton.vue';
import movePostviewButton from '~/components/movePostviewButton.vue';

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
    <MovePostviewButton />
    <div class="timeLine">
        <div v-for="id in ids" :key="id" class="postContents">
            <PostView class="postView" :id="id"/>
        </div>
    </div>
</template>

<style scoped>
.timeLine {
    padding: 10px;
    background-color: #ffffff;
}
.postView {
    margin: 5%;
}
</style>