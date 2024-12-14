<template>
    <a :href="`/test/${id}`">
        <div class="postView">
            <img v-if="imagefilename" :src="`${endpoint}image/${imagefilename}`">
            <div class="contents">
                <h1>{{ title }}</h1>
                <p>{{ description }}</p>
            </div>
            <div class="account">
                <div class="icon"></div>
                <p>{{ username }}</p>
            </div>

        </div>
    </a>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New&display=swap');
/* font-family: "Zen Kaku Gothic New", sans-serif; */
a {
    text-decoration: none;
    color: black;
}
img {
    width: 100%;
    max-height: 100px;
    object-fit: cover;
    border-radius: 20px 20px 0px 0px;
}
.postView {
    background-color: #f5f5f5;
    border-radius: 20px;
}
h1 {
    margin: 0px;
    padding: 0px;
    font-size: 140%;
}
.contents {
    padding-top: 5px;
    text-align: center;
    font-family: "Zen Kaku Gothic New", sans-serif;
    padding-left: 30px;
    padding-right: 30px;
}
.contents p {
    margin: 0px;
}
.account {
    font-family: "Zen Kaku Gothic New", sans-serif;
    padding: 3px 30px 10px 30px;
    border-top: 1px solid #dcdcdc;
    margin-top: 5px;
}
.account p {
    margin: 0px;
}
</style>

<script>
import{endpoint} from '~/components/APIEndPoint'

export default {
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            title: '',
            description: '',
            username: '',
            endpoint: endpoint
        }
    },
    async created() {
        const response = await fetch(endpoint+`idea/${this.id}`, {
        })
        const data = await response.json()
        this.title = data.idea.title
        this.description = data.idea.description
        this.username = data.username
        this.imagefilename = data.idea.image
    },
}

</script>