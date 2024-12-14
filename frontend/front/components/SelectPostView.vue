<template>
    <div class="postView" @click="emitItemClick">
        <img v-if="imagefilename" :src="`${endpoint}image/${imagefilename}`">
        <div class="contents">
            <h1>{{ title }}</h1>
            <p>{{ truncatedDescription }}</p>
        </div>
        <div class="account">
            <div class="icon"></div>
            <p>{{ username }}</p>
        </div>
    </div>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New&display=swap');

.postView {
    border-radius: 15px;
    background-color: #fff;
    color: black;
    text-decoration: none;
    margin: 5%;
}
img {
    width: 100%;
    max-height: 100px;
    object-fit: cover;
    border-radius: 20px 20px 0px 0px;
}
h1 {
    font-family: "Zen Kaku Gothic New", sans-serif;
    margin: 0;
    padding: 0;
    font-size: 20px;
}
p {
    font-family: "Zen Kaku Gothic New", sans-serif;
    margin: 0;
    padding: 0;
}
.contents {
    padding: 5px;
}
.account {
    border-top: 1px solid #bdbdbd;
    padding: 5px;
    display: flex;
}
.icon p {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
.icon {
    border-radius: 50%;
    height: 20px;
    width: 20px;
    background-color: black;
    margin-right: 5px;
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
    computed: {
        truncatedDescription() {
            return this.description.length > 40 ? this.description.substring(0, 40) + '...' : this.description;
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
    methods: {
        emitItemClick() {
            this.$emit('item-click', this.id, this.title, this.description);
        }
    }
}

</script>